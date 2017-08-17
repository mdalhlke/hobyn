#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.appengine.api import users
from models import *
from datetime import date
import webapp2
import jinja2
from google.appengine.api import users


env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template= env.get_template('home.html')
        user = users.get_current_user()
        logout_url= users.create_logout_url('/')
        login_url= users.create_login_url('/')
        var ={}
        if user:
            var ['greeting'] = ('<a href="%s">Sign out</a>' % logout_url)
        else:
            var ['greeting'] = ('<a href="%s">Sign In or Register</a>' % login_url)
        if users.get_current_user():
            email=users.get_current_user().email()
            user=User.query(User.email==email).fetch()
            if user:
                pass
            else:
                user= User(
                    name=users.get_current_user().nickname(),
                    email=users.get_current_user().email()
                    )
                user.put()

        self.response.write(template.render(var))

class PersonalityTestHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('personality_test.html')
        query = Question.query().order()
        questions = query.fetch()
        var = {
            'questions': questions
        }

        self.response.write(template.render(var))

class UserProfileHandler(webapp2.RequestHandler):
    def sort_insertion(my_list):
        for i in range(1,len(my_list)):
            val_current = my_list[i]
            pos = i
            # check backwards through sorted list for proper pos of val_current
            while((pos > 0) and (my_list[pos-1] > val_current)):
                my_list[pos] = my_list[pos-1]
                pos = pos-1
            if pos != i:
                my_list[pos] = val_current
        return my_list

    def post(self):
        template = env.get_template('user_profile.html')
        N,O,A,C,E=0,0,0,0,0
        for i in range(0, len(Question.query().fetch())):
            value=self.request.get("answer_"+str(i))
            if value=="N":
                N= N+1
            elif value=="O":
                O=O +1
            elif value=="A":
                A=A +1
            elif value=="C":
                C=C +1
            else:
                E=E +1
        user=users.get_current_user()
        if user:
            user=User.query(User.email== user.email()).get()
            user.N_points=N
            user.O_points=O
            user.A_points=A
            user.C_points=C
            user.E_points=E
            user.put()
        else:
            self.response.write("no user logged in")
        self.response.write(template.render())
    def get(self):
        template= env.get_template('user_profile.html')
        user=User.query(User.email == users.get_current_user().email()).get()
        hobby_lists=[]
        keys =["N_points","O_points","A_points","C_points","E_points"]
        for i in range(1,len(keys)):
            val_current= getattr(user,keys[i])
            pos =i
            string_value= keys[pos]
            while((pos>0)and (getattr(user,keys[pos-1])<val_current)):
                keys[pos]= keys[pos-1]
                keys[pos-1]=string_value
                pos=pos-1
                string_value= keys[pos]
                #self.response.write(keys)
            setattr(user,keys[pos],val_current)
        #self.response.write(keys)

        for i in range(0,2):
            query= Hobby.query(getattr(Hobby,keys[i])<=getattr(user,keys[i])).order(getattr(Hobby,keys[i])).fetch()
            hobby_lists.append(query)
        self.response.write(template.render({'hobby_lists':hobby_lists}))
    #example function
        #for i in range(1,len(my_list)):
        #    val_current = my_list[i]
        #    pos = i
        #    # check backwards through sorted list for proper pos of val_current
        #    while((pos > 0) and (my_list[pos-1] > val_current)):
        #        my_list[pos] = my_list[pos-1]
        #        pos = pos-1
        #    if pos != i:
        #        my_list[pos] = val_current
        #return my_list
    #end example

class MakeHobbyHandler(webapp2.RequestHandler):
    def post(self):
        template = env.get_template('create_hobby.html')
        var = {
            'name':self.request.get('name'),
            'N': int(self.request.get('N_points')),
            'O': int(self.request.get('O_points')),
            'A': int(self.request.get('A_points')),
            'C': int(self.request.get('C_points')),
            'E': int(self.request.get('E_points')),
            'description': self.request.get('description'),
        }

        hobby= Hobby(name=var['name'],
                          N_points= var['N'],
                          O_points= var['O'],
                          A_points= var['A'],
                          C_points= var['C'],
                          E_points= var['E'],
                          description= var['description'],
                          )
        key= hobby.put()
        self.response.write(template.render(var))
    def get(self):
        template=env.get_template('pre_create_hobby.html')
        self.response.write("I")
        self.response.write(template.render())

class PersonalHobbyHandler(webapp2.RequestHandler):
    def get(self):
        template= env.get_template('hobby.html')
        #name
        var={
            'name':self.request.get('name')
        }
        hobby=Hobby.query(Hobby.name==var['name']).get()
        var['description']=hobby.description

        #Message
        query = Message.query(Message.hobby_key == hobby.key)
        query_results=query.fetch()
        var['content']= query_results

        self.response.write(template.render(var))

    def post(self):
        template= env.get_template('hobby.html')
        #name
        var={
            'name':self.request.get('name')
        }
        hobby=Hobby.query(Hobby.name==var['name']).get()
        var['description']=hobby.description

        #Message
        user= User.query(User.email==users.get_current_user().email()).get()

        if self.request.get('content'):
            message=Message(
                content= self.request.get('content'),
                user_key = user.key,
                hobby_key= hobby.key
            )
            key= message.put()
            self.redirect("/personal_hobby?name="+var['name'])
        query = Message.query(Message.hobby_key == hobby.key)
        query_results=query.fetch()
        var['content']= query_results

        self.response.write(template.render(var))


class AllHobbiesHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('all_hobbies.html')
        query = Hobby.query().order()
        hobbies = query.fetch()
        print(hobbies)
        var = {
            'hobbies': hobbies
        }
        self.response.write(template.render(var))

class QuestionHandler(webapp2.RequestHandler):
    def post(self):
        template = env.get_template('create_question.html')
        var = {
            'text':self.request.get('question_text'),
            'N':self.request.get('N_option'),
            'O': self.request.get('O_option'),
            'A': self.request.get('A_option'),
            'C': self.request.get('C_option'),
            'E': self.request.get('E_option')
        }

        question= Question(question_text=var['text'],
                          N_option= var['N'],
                          O_option= var['O'],
                          A_option= var['A'],
                          C_option= var['C'],
                          E_option= var['E'],
                          )
        key= question.put()
        self.response.write(template.render(var))
    def get(self):
        template=env.get_template('pre_create_question.html')
        self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/personality_test', PersonalityTestHandler),
    ('/user_profile', UserProfileHandler),
    ('/make_hobby', MakeHobbyHandler),
    ('/personal_hobby', PersonalHobbyHandler),
    ('/all_hobbies', AllHobbiesHandler),
    ('/make_question',QuestionHandler),
    #('/hobby',HobbyHandler),

], debug=True)

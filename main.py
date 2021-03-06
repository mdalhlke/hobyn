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
    def post(self):
        template = env.get_template('recommendation.html')
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
            self.redirect("/user_profile")
        else:
            self.response.write("no user logged in")
        #self.response.write("<p> this is post</p>")
        self.response.write(template.render())
    def get(self):
        template= env.get_template('recommendation.html')
        user=User.query(User.email == users.get_current_user().email()).get()

        hobby_list=[]
        hobbies=Hobby.query().fetch()
        for hobby in hobbies:
            points=0
            minimum=3
            if  hobby.N_points < user.N_points and 0!=hobby.N_points:
                points= points+1
            if  hobby.O_points < user.O_points and 0!=hobby.O_points:
                points= points+1
            if  hobby.A_points < user.A_points and 0!=hobby.A_points:
                points= points+1
            if  hobby.C_points < user.C_points and 0!=hobby.C_points:
                points= points+1
            if  hobby.E_points < user.E_points and 0!=hobby.E_points:
                points= points+1
            if points>=minimum:
                hobby_list.append(hobby)
        #self.response.write("<p> this is get</p>")
        self.response.write(template.render({'hobby_list':hobby_list}))


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
            'image': self.request.get('image'),
        }

        hobby= Hobby(name=var['name'],
                          N_points= var['N'],
                          O_points= var['O'],
                          A_points= var['A'],
                          C_points= var['C'],
                          E_points= var['E'],
                          description= var['description'],
                          image= var['image'],
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

        var={
            'name':self.request.get('name')
        }
        hobby=Hobby.query(Hobby.name==var['name']).get()
        var['description']=hobby.description
        var['image']=hobby.image


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
        var['image']=hobby.image

        #Message
        if users.get_current_user():
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
        template= env.get_template('pre_create_question.html')
        self.response.write(template.render())
        
class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("about_us.html")
        
        self.response.write(template.render())
<<<<<<< HEAD
=======

class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('about_us.html')
        self.response.write(template.render())

>>>>>>> 3b21c47abea99b7f6eee20c9955a52adc6c90bd7

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/personality_test', PersonalityTestHandler),
    ('/user_profile', UserProfileHandler),
    ('/make_hobby', MakeHobbyHandler),
    ('/personal_hobby', PersonalHobbyHandler),
    ('/all_hobbies', AllHobbiesHandler),
    ('/make_question',QuestionHandler),
<<<<<<< HEAD
    ('/about', AboutHandler),
=======
    ('/about_us',AboutUsHandler),
>>>>>>> 3b21c47abea99b7f6eee20c9955a52adc6c90bd7
], debug=True)

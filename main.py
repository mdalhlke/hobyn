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

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('home.html')
        self.response.write(template.render())

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template= env.get_template('home.html')
        user = users.get_current_user()
        logout_url= users.create_logout_url('/')
        login_url= users.create_login_url('/')
        var ={}
        if user:
            var ['greeting'] = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                (user.nickname(), logout_url))
        else:
            var ['greeting'] = ('<a href="%s">Sign in or register</a>.' %
                login_url)

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
    def get(self):
        template = env.get_template('user_profile.html')
        for i in range(0, len(Question.query().fetch())):
            value=self.request.get("answer_"+str(i))
        
        self.response.write(self.request.get("answer_0"))
            
        self.response.write(template.render())

class HobbyHandler(webapp2.RequestHandler):
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
        self.response.write(template.render())

class PersonalHobbyHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('hobby.html')
        self.response.write(template.render())

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
    ('/login', LoginHandler),
    ('/personality_test', PersonalityTestHandler),
    ('/user_profile', UserProfileHandler),
    ('/hobby', HobbyHandler),
    ('/personal_hobby', PersonalHobbyHandler),
    ('/all_hobbies', AllHobbiesHandler),
    ('/make_question',QuestionHandler),

], debug=True)

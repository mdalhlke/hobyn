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

class FormHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('form.html')
        self.response.write(template.render())

class UserProfileHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('user_profile.html')
        self.response.write(template.render())

class HobbyHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('hobby.html')
        self.response.write(template.render())

class AllHobbiesHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('all_hobbies.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LoginHandler),
    ('/form', FormHandler),
    ('/user_profile', UserProfileHandler),
    ('/hobby', HobbyHandler),
    ('/all_hobbies', AllHobbiesHandler),
    
], debug=True)

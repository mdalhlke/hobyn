from google.appengine.ext import ndb
class User(ndb.Model):
    name= ndb.StringProperty()
    email= ndb.StringProperty()
    avatar= ndb.BlobProperty()
    date_created= ndb.DateProperty()
    friends= ndb.StringProperty()
    N_points= ndb.IntegerProperty()
    O_points= ndb.IntegerProperty()
    A_points= ndb.IntegerProperty()
    C_points= ndb.IntegerProperty()
    E_points= ndb.IntegerProperty()

class Hobby(ndb.Model):
    name= ndb.StringProperty()
    description= ndb.StringProperty()
    image= ndb.BlobProperty()
    N_points= ndb.IntegerProperty()
    O_points= ndb.IntegerProperty()
    A_points= ndb.IntegerProperty()
    C_points= ndb.IntegerProperty()
    E_points= ndb.IntegerProperty()

class Message(ndb.Model):
    user_key= ndb.KeyProperty()
    date_received= ndb.DateProperty()
    title= ndb.StringProperty()
    content= ndb.StringProperty()

class Friend(ndb.Model):
    follower_key= ndb.KeyProperty()
    followee_key= ndb.KeyProperty()

class Question(ndb.Model):
    question_text= ndb.StringProperty()
    N_option= ndb.StringProperty()
    O_option= ndb.StringProperty()
    A_option= ndb.StringProperty()
    C_option= ndb.StringProperty()
    E_option= ndb.StringProperty()

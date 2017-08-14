from google.appengine.ext import ndb
class User(ndb.Model):
    name= ndb.StringProperty()
    username= ndb.StringProperty()
    avatar= ndb.BlobProperty()
    date_created= ndb.DateProperty()
    friends= ndb.StringProperty()
    N_points= ndb.IntegerProperty()
    O_points= ndb.IntegerProperty()
    A_points= ndb.IntegerProperty()
    C_points= ndb.IntegerProperty()
    E_points= ndb.IntegerProperty()

class Hobby:
    name= ndb.StringProperty()
    description= ndb.StringProperty()
    image= ndb.BlobProperty()
    N_points= ndb.IntegerProperty()
    O_points= ndb.IntegerProperty()
    A_points= ndb.IntegerProperty()
    C_points= ndb.IntegerProperty()
    E_points= ndb.IntegerProperty()

class Message:
    user_key= ndb.KeyProperty()
    date_received= ndb.DateProperty()
    title= ndb.StringProperty()
    content= ndb.StringProperty()

class Friend:
    follower_key= ndb.KeyProperty()
    followee_key= ndb.KeyProperty()

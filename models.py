from google.appengine.ext import ndb
class User(ndb.Model):
    name= ndb.StringProperty()
    username= ndb.StringProperty()
    avatar= ndb.BlobProperty()
    date_created= ndb.DateProperty()
    friends= ndb.StringProperty()
    avatar= ImageProperty()
    N-points= ndb.IntegerProperty()
    O-points= ndb.IntegerProperty()
    A-points= ndb.IntegerProperty()
    C-points= ndb.IntegerProperty()
    E-points= ndb.IntegerProperty()
    
class Hobby:
    name= ndb.StringProperty()
    description= ndb.StringProperty()
    image= ndb.BlobProperty()
    N-points= ndb.IntegerProperty()
    O-points= ndb.IntegerProperty()
    A-points= ndb.IntegerProperty()
    C-points= ndb.IntegerProperty()
    E-points= ndb.IntegerProperty()
    
class Message:
    user_key= ndb.KeyProperty()
    date_received= ndb.DateProperty()
    title= ndb.StringProperty()
    content= ndb.StringProperty()

class Friend:
    follower_key= ndb.KeyProperty()
    followee_key= ndb.KeyProperty()
    
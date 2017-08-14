from google.appengine.ext import ndb
class User(ndb.Model):
    name= ndb.StringProperty()
    username= ndb.StringProperty()
    avatar= ndb.BlobProperty()
    date_created= ndb.DateProperty()
    friends= ndb.StringProperty()
    avatar= ImageProperty()
    N-points= ndb.IntProperty()
    O-points= ndb.IntProperty()
    A-points= ndb.IntProperty()
    C-points= ndb.IntProperty()
    E-points= ndb.IntProperty()
    
class Hobby:
    name= ndb.StringProperty()
    description= ndb.StringProperty()
    image= ndb.BlobProperty()
    N-points= ndb.IntProperty()
    O-points= ndb.IntProperty()
    A-points= ndb.IntProperty()
    C-points= ndb.IntProperty()
    E-points= ndb.IntProperty()
    
class Message:
    user_key= ndb.KeyProperty()
    date_received= ndb.DateProperty()
    title= ndb.StringProperty()
    content= ndb.StringProperty()

class Friend:
    follower_key= ndb.KeyProperty()
    followee_key= ndb.KeyProperty()
    
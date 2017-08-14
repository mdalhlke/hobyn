from google.appengine.ext import ndb
class User(ndb.Model):
    name= ndb.StringProperty()
    username= ndb.StringProperty()
    date_created= ndb.DateProperty()
    friends= ndb.StringProperty()
    avatar= ImageProperty()
class Hobby:
    name= ndb.StringProperty()
    description= ndb.StringProperty()
    N-points= ndb.IntProperty()
    O-points= ndb.IntProperty()
    A-points= ndb.IntProperty()
    C-points= ndb.IntProperty()
    E-points= ndb.IntProperty()
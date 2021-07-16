from google.appengine.ext import ndb

class Invitado(ndb.Model):
    nombre = ndb.StringProperty(required=True )
    hora = ndb.DateTimeProperty(indexed = True,auto_now_add=True )

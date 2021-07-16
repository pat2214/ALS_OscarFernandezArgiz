#asignatura pertenece a un curso

from google.appengine.ext import ndb

class Item(ndb.Model):
    nombre = ndb.StringProperty(required=True)
    numero = ndb.StringProperty(required=True)
    cantidad = ndb.IntegerProperty(indexed=True)

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["it"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()

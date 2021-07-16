from google.appengine.ext import ndb

from item import Item

class Vendedor(ndb.Model):

    nombre = ndb.StringProperty(indexed = True)
    direccion = ndb.StringProperty(indexed=True)
    pedidoMax = ndb.IntegerProperty(indexed=True)
    telefono = ndb.IntegerProperty()
    clave_item = ndb.KeyProperty(kind=Item)
    @staticmethod
    def recupera_para(req):
        try:
            #primera parte de la url solo con la id del itemVend
           id_item = req.GET["itVend"]
        except KeyError:
            id_item = ""

        if id_item:
            calve_item = ndb.Key(urlsafe=id_item)
            vendedores = Vendedor.query(Vendedor.clave_item == calve_item)
            return (calve_item.get(),vendedores)
        else:
            print ("ERRIR: vendedor no encontrado")

    @staticmethod
    def recupera_vendedor(req):
        try:
            id = req.GET["vend"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()

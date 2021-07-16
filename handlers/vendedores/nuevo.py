# coding: utf-8
from google.appengine.ext import ndb
import webapp2
from webapp2_extras import jinja2
from model.vendedor import Vendedor
import time

class NuevoVendedorHandler(webapp2.RequestHandler):
    def get(self):
        valores_plantilla = {
            "clave_item" : self.request.GET["itVend"]
         }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("nuevo_vendedor.html",
            **valores_plantilla))
    def post(self):
        nombre = self.request.get("edNombre", "")
        direccion = self.request.get("edDir", "")
        str_pedidoMax = self.request.get("edPedidoMax", "")
        clave_item = self.request.GET["itVend"]
        str_telefono = self.request.get("edTelefono", "")

        try:
            pedidoMax = int(str_pedidoMax)

        except ValueError:
            pedidoMax = -1

        try:
            telefono = int(str_telefono)

        except ValueError:
            telefono = -1

        if (not nombre or not direccion or pedidoMax<0 or telefono<0):
                    return self.redirect("/")
        else:

            vendedor = Vendedor(nombre=nombre,
                                direccion=direccion,
                                pedidoMax=pedidoMax,
                                telefono=telefono,
                                clave_item=ndb.Key(urlsafe=clave_item))

            vendedor.put()
            time.sleep(1)
            return self.redirect("/vendedores/lista?itVend="+ clave_item)

app = webapp2.WSGIApplication([
    ('/vendedores/nuevo', NuevoVendedorHandler)
], debug=True)

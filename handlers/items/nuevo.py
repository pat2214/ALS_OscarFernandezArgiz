# coding: utf-8
#nueva Asignatura

import webapp2
from webapp2_extras import jinja2
from model.item import Item
import time

class NuevoItemHandler(webapp2.RequestHandler):
    def get(self):
        valores_plantilla = {

         }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("nuevo_item.html",
            **valores_plantilla))
    def post(self):
        nombre = self.request.get("edNombre", "")
        numero = self.request.get("edNumero", "")
        str_cantidad = self.request.get("edCant", "")

        try:
            cantidad = int(str_cantidad)

        except ValueError:
            cantidad = -1


        if (not(numero)or cantidad < 0 or not (nombre)):
                    return self.redirect("/")
        else:

            item = Item(nombre=nombre,cantidad=cantidad, numero=numero)
            item.put()
            time.sleep(1)
            return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/items/nuevo', NuevoItemHandler)
], debug=True)

#!/usr/bin/env python
#

import webapp2
from webapp2_extras import jinja2

from model.vendedor import Vendedor

class ListaVendedoresHandler(webapp2.RequestHandler):
    def get(self):
        item, vendedores = Vendedor.recupera_para(self.request)

        valores_plantilla = {
            "item" : item,
            "vendedores" : vendedores
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("lista_vendedores.html", **valores_plantilla))

app = webapp2.WSGIApplication([
    ('/vendedores/lista', ListaVendedoresHandler)
], debug=True)

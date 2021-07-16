import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.item import Item
from model.invitado import Invitado

class MainHandler(webapp2.RequestHandler):
    def get(self):

        jinja = jinja2.get_jinja2(app=self.app)
        usr = users.get_current_user()
        items = Item.query().order(-Item.numero)

        invitados = Invitado.query().order(-Invitado.hora)
        invitado = Invitado(nombre=str(usr))
        invitado.put()

        if usr:
            # en caso de que si haya usuario va a /
            url_usr = users.create_logout_url("/ ")
        else:
            #en caso de que no haya usuario va a /
            url_usr = users.create_login_url("/ ")

        valores_plantilla = {
            "usr":usr,
            "url_usr":url_usr,
            "items": items,
            "invitados": invitados
        }

        self.response.write(jinja.render_template("index.html",**valores_plantilla))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
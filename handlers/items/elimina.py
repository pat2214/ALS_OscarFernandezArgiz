# coding: utf-8
#nueva Asignatura

import webapp2

from model.item import Item
import time

class EliminaItemHandler(webapp2.RequestHandler):
    def get(self):
        item = Item.recupera(self.request)
        # (ndb.Key(urlsafe=id).get()).key.delete()
        item.key.delete()
        time.sleep(1)
        return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/items/elimina', EliminaItemHandler)
], debug=True)

#!/usr/bin/env python

import webapp2

from basic.handlers import MainHandler
from basic.handlers import AboutHandler
from printing.handlers import PrintersHandler


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name='index'),
    webapp2.Route('/printing', PrintersHandler, name='printing'),
    webapp2.Route('/about', AboutHandler, name='about'),
], debug=True)

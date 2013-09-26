import os
import webapp2
import jinja2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)


#this is how to make comments in python

class Welcome(BaseHandler):
    def get(self):
        self.render('welcome.html')

class About(BaseHandler):
    def get(self):
        self.render('about.html')

class Carousel(BaseHandler):
    def get(self):
        self.render('./examples/carousel/index.html')
class Grid(BaseHandler):
    def get(self):
        self.render('./examples/grid/index.html')
class Jumbotron(BaseHandler):
    def get(self):
        self.render('./examples/jumbotron/index.html')
class JumbotronNarrow(BaseHandler):
    def get(self):
        self.render('./examples/jumbotron-narrow/index.html')
class JustifiedNav(BaseHandler):
    def get(self):
        self.render('./examples/justified-nav/index.html')
class Navbar(BaseHandler):
    def get(self):
        self.render('./examples/navbar/index.html')

class NavbarFixedTop(BaseHandler):
    def get(self):
        self.render('./examples/navbar-fixed-top/index.html')
class NavbarStaticTop(BaseHandler):
    def get(self):
        self.render('./examples/navbar-static-top/index.html')
class NonResponsive(BaseHandler):
    def get(self):
        self.render('./examples/non-responsive/index.html')
class OffCanvas(BaseHandler):
    def get(self):
        self.render('./examples/offcanvas/index.html')
class Screenshots(BaseHandler):
    def get(self):
        self.render('./examples/Screenshots/index.html')
class Signin(BaseHandler):
    def get(self):
        self.render('./examples/signin/index.html')
class StarterTemplate(BaseHandler):
    def get(self):
        self.render('./examples/starter-template/index.html')
class StickyFooter(BaseHandler):
    def get(self):
        self.render('./examples/sticky-footer/index.html')
class StickyFooterNavbar(BaseHandler):
    def get(self):
        self.render('./examples/sticky-footer-navbar/index.html')
class Theme(BaseHandler):
    def get(self):
        self.render('./examples/theme/index.html')
app = webapp2.WSGIApplication([('/', Welcome)
                              ,('/about', About)
                              ,('/carousel',Carousel)
                              ,('/grid',Grid)
                              ,('/jumbotron',Jumbotron)
                              ,('/jumbotron-narrow',JumbotronNarrow)
                              ,('/justified-nav',JustifiedNav)
                              ,('/navbar',Navbar)
                              ,('/navbar-fixed-top',NavbarFixedTop)
                              ,('/navbar-static-top',NavbarStaticTop)
                              ,('/non-responsive',NonResponsive)
                              ,('/offcanvas',OffCanvas)
                              ,('/screenshots',Screenshots)
                              ,('/signin',Signin)
                              ,('/starter-template',StarterTemplate)
                              ,('/sticky-footer',StickyFooter)
                              ,('/sticky-footer-navbar',StickyFooterNavbar)
                              ,('/theme',Theme)
                              ], debug=True)

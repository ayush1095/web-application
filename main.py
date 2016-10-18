import webapp2
import jinja2
from google.appengine.ext import db
template_dir= os.path.join(os.path.dirname(__file__),'templates')
jinja_env= jinja2.Environment(loader=jinja2.FileSystemloader(template_dir),
                              autoescape= True)
def render_str(template, **params):
     t=jinja_env.get_template(template)
     return t.render(params)
class BaseHandler(webapp2.RequestHandler):
    def render(self,template,**kw):
        self.response.out.write(render_str(template,**kw))

    def write(self,*a,**kw):
        self.response.out.write(*a,**kw)

class Rot13(BaseHandler):
    def get(self):
        self.render('rot13.html')

    def post(self):
        rot13=''
        text=self.request.get('text')
        if text:
            rot13=text.encode('rot13')
class Welcome(BaseHandler):
    def get(self):
        username=self.request.get('username')
        if valid_username(username):
            self.render('welcome.html',username=username)
        else:
            self.redirect('/signup')

        self.render('rot13.html',text=rot13)
app=webapp2.WSGIApplication([('/rot13',Rot13),
                             ('/signup',Signup),
                             ('/welcome',Welcome)],
                            debug=True)

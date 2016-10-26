import os
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
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

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
        self.render('rot13.html',text=rot13)

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)


PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIl_RE = re.compile(r'^[\s]+@[\s]+\.[\s]+$')
def valid_email(email):
    return not email or EMAIl_RE.match(email)




class Signup(BaseHandler):
    def get(self):
        self.render("signup.html")

    def post(self):
        have_error=False
        username=self.request.get('username')
        password=self.request.get('password')
        verify=self.request.get('verify')
        email=self.request.get('email')

        params=dict(username=username,
                    email=email)


''' functions valid_username, valid_email, valid_password yet to be declared '''




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

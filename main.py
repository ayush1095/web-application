import webapp2
form="""


def escape_html(s):

 for (i,o) in (("&", "&amp;"),
              ('"',  "&quote;"),
              ("<", "&lt;"),
              (">", "&gt;")):
    s=s.replace(i,o)
 return s
print escape_html("escaping added")

class MainPage(webapp2.RequestHandler):
 def get(self):
     self.response.out.write(form)
app=webapp2.WSGIApplication([('/',MainPage)])

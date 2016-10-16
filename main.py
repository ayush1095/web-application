import webapp2
import cgi
form="""

<html>
  <head>
    <title>Unit 2 Rot 13</title>
  </head>

  <body>
    <h2>Enter some text to ROT13:</h2>
    <form method="post" action="/testform">
      <textarea name="text"
                style="height: 100px; width: 400px;"></textarea>
      <br>
      <input type="submit">
    </form>
  </body>

</html>
"""

class MainPage(webapp2.RequestHandler):
 def get(self):
     self.response.out.write(form)
 def escape_html(s):
     return cgi.escape(text, quote=True)
class TestHandler(webapp2.RequestHandler):
 def post(self):
     text=self.request.get("text")
     q= escape_html(text)
     self.response.out.write(q)
app=webapp2.WSGIApplication([('/',MainPage),('/testform',TestHandler)],
                            debug=True)

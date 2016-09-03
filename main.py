import webapp2
form="""

<html>
  <head>
    <title>Unit 2 Rot 13</title>
  </head>

  <body>
    <h2>Enter some text to ROT13:</h2>
    <form method="post">
      <textarea name="text"
                style="height: 100px; width: 400px;"></textarea>
      <br>
      <input type="submit">
    </form>
  </body>

</html>
"""
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

# Russell Schlup
# January 22, 2014
# DPW
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	#read
        url = 'source.txt'
        result = open(url, 'r')
        self.response.write(result.read())

        #write
        result2 = open(url, 'w') # 'a' everything
        result2.write('what does it do?')
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
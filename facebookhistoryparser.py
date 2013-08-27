import sys
sys.path.insert(0, 'libs')
import os
import urllib

import jinja2
import webapp2

from bs4 import BeautifulSoup
from facebookHtmlParse import facebookHtmlParse
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
    extensions=['jinja2.ext.autoescape'])

userInput = ""
htmlParser = facebookHtmlParse()
class MainPage(webapp2.RequestHandler):

    def get(self):
        upload_url = blobstore.create_upload_url('/upload')
        template_vars = { 'upload_url' : upload_url }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_vars))

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        # Get file from user
        upload_files = self.get_uploads('file') # 'file' is file upload field in the form
        blob_info = upload_files[0]
        # Put file in string object
        blob_reader = blobstore.BlobReader(blob_info.key())
        global userInput
        userInput = blob_reader.read()
        blob_reader.close()
        # Delete original file
        blob_info.delete()
        # Send the string object (it's global) forward in process chain
        self.redirect('/findUsers')

class FindUsersHandler(webapp2.RequestHandler):
    def get(self):
        global userInput
        global htmlParser
        htmlParser.loadString(userInput)
        htmlParser.buildSoup()
        htmlParser.buildThreads()
        names = htmlParser.getNamesList()
        
        template_vars = {'names' : names}
        template = JINJA_ENVIRONMENT.get_template('findUsers.html')
        self.response.write(template.render(template_vars))


class ParseMessagesHandler(webapp2.RequestHandler):
    def post(self):
        global htmlParser
        names = self.request.get_all("user")
        afterParseHtml = htmlParser.extractRequired(names)
        self.response.write(afterParseHtml)

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/upload', UploadHandler),
    ('/findUsers', FindUsersHandler),
    ('/parseMessages', ParseMessagesHandler),
], debug=True)

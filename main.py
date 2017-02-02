#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import validate

def build_page(self):

    username = "Username:<input style='width: 100px' name='username'/>"

    password = "Password:<input type='password' style='width: 100px' name='password'/>"

    confirm = "Confirm:<input type='password' style='width: 100px' name='confirm'/>"

    email = "E-mail:<input style='width: 100px' name='email'/>"

    submit = "<input type='submit'/>"



    form = ("<form method='post'>" + username + "<br>" + password + "<br>" + confirm + "<br>" + email + "<br>" + submit + "</form>")
    header = "<h2>Username and Password</h2>"

    return header + form


class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")
        self.response.write(content)

    def post(self):
        user = cgi.escape(self.request.get("username"))
        uvalid = validate.user_valid(user)
        password = cgi.escape(self.request.get("password"))
        pvalid = validate.pass_valid(password)
        confirm = cgi.escape(self.request.get("confirm"))
        cvalid = validate.conf_valid(confirm, password)
        email = cgi.escape(self.request.get("email"))
        evalid = validate.emai_valid(email)
        valid = ""
        #congrats =
        if uvalid == True and pvalid == True and cvalid == True and evalid == True:
            self.redirect("/welcome")
        else:
            if uvalid != True:
                valid = uvalid

            if pvalid != True:
                valid += pvalid

            if cvalid != True:
                valid += cvalid

            if evalid != True:
                valid += evalid
        content = build_page(self)
        contents = content + valid
        self.response.write(contents)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        user = self.request.get("username")
        sentance = "Welcome," + user + "!"
        #welcome_content = "<form method='post'>Welcome,"'<h1>' + user + '</h1>'"!</form>"

        self.response.write(sentance)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)

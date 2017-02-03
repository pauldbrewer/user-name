import re
import logging

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def user_valid(user):
    if user and (USER_RE.match(user) != None):
        return True
    else:
        return "Enter a valid Username"

def pass_valid(pas):
    if pas and (PASS_RE.match(pas) != None):
        return True
    else:
        return "Enter valid Password"

def conf_valid(con, pas):
    if con and con == pas:
        return True
    else:
        return "Must match Password"

def emai_valid(email):
    if email and (EMAIL_RE.match(email)) != None:
        return True
    else:
        return "Enter valid E-Mail"

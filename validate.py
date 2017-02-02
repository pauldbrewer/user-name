

def user_valid(user):
    if user:
        return True
    else:
        return "Enter a valid Username"

def pass_valid(pas):
    if pas:
        return True
    else:
        return "Enter valid Password"

def conf_valid(con, pas):
    if con and con == pas:
        return True
    else:
        return "Must match Password"

def emai_valid(email):
    if email:
        return True
    else:
        return "Enter valid E-Mail"

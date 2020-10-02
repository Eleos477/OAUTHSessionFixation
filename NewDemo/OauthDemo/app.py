# This class is a copy of __init__.py but works with the docker
# __init__ class has import problems but this one is compatible

import os
import pickle
import sys
import requests

from flask import Flask, render_template, request, redirect, url_for, session, flash
from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField
# from form import LoginForm


##############################################
### INITIALISE GLOBAL APPLICATION VARIABLE ###
##############################################
# app = None
app = Flask(__name__)
app.secret_key = '!secret'
app.config.from_object('config')


# def initialiseApp(test_config=None):
#     """Initialises the application with a given configuration (useful for testing)."""
#     global app
    
#     #App creation
#     app = Flask(__name__)
#     app.secret_key = '!secret'

#     if test_config is None:
#         app.config.from_object('config')
#     else: # If test configuration imported, use this special configuration
#         app.config.update(test_config)

#     return app

# app = initialiseApp()

## Remaining imports
#Package for registration page
# import OAUTH.registration
import registration
from banking import *

# #Package for objects
# import OAUTH.objects
from objects import *

import model

############################
## INTERNAL DOCUMENTATION ##
############################
# Session Information:
#   Sessions are stored as custom Session objects which contain a unique identifier and the associated customer. 
#   The session ID is stored in the session as "SESSION_ID".

#########################
## RUNTIME STARTS HERE ##
#########################
#Check for existing data & load - can use as standin for database - use code from old demo
model.loadRegisteredUsers()
print("LOADED ALL REGISTERED USERS - here they are:")
[print(user.accountNum) for user in model.registeredUsers] #TODO get rid of this


#Default page
@app.route('/', methods=["GET","POST"])
def index():
    print("ENTERED INDEX PAGE")
    
    model.manageSession(session, request.args.get('session'))
    if model.validateSession(session): # If user session exists
        user = model.findUser(model.sessions[session['SESSION_ID']].accountNum) # Get the user by customer number

        print(f"DEBUG: Index - user session is {session['SESSION_ID']}")
        print(f"Initiated index for user '{user.accountNum}'")

        return render_template('index.html', name=(user.name + ' ' + user.surname), number=user.accountNum, balance=user.account.balance)
    else:
        return redirect('/login')


@app.route('/login', methods=["GET","POST"])
def login():
    #Create login form, both fields are mandatory -- user input fields are not centred for some reason
    # print(repr(login.accountNum))
    model.manageSession(session, request.args.get('session'))
    if not model.validateSession(session): # If customer not already logged in
        login = LoginForm(request.form)

        if request.method == "POST":
            #Debug print
            print(f"Attempted login with account '{login.accountNum}', password '{login.password.data}'", file=sys.stdout)

            # Try to find a user with input username & password
            user = model.validateUser(int(login.accountNum.data), login.password.data)

            print(f"DEBUG: Tried to get user and got {user}", file=sys.stdout)

            # If a user with the given username and password was found
            if (user is not None):
                # Debug print
                print(f"Login for {login.accountNum.data} accepted!", file=sys.stdout)

                # Create a session object for this new session (which is now stored in the dict of session objects)
                model.createUserSession(session, user)

                #On successful login, will redirect to that user's profile
                return redirect('/')
            else:
                flash("Invalid username or password")
        return render_template('login.html', form=login)
    else: # If customer already logged in
        return redirect('/')

@app.route('/logout', methods=["GET", "POST"])
def logout():
    """Logs out a user from the application by removing their session and invalidating their session ID."""
    model.manageSession(session, request.args.get('session'))
    if (model.validateSession(session)):
        print("Logging out a user...")
        
        # Clear the current session
        session.clear()

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000, threaded=True)

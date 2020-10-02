
import pickle
import os
import string
import random
from objects import Session
from app import app

########################
### Registered Users ###
########################
registeredUsers = []
# TODO REPLACE THE LIST OF USERS WITH A DICTIONARY BECAUSE THAT MAKES WAY MORE SENSE

def addRegisteredUser(user):
    """Adds the imported user to the list of users"""
    registeredUsers.append(user)

def loadRegisteredUsers():
    filepath = app.config["REGISTERED_USERS_SAVE"]
    if os.path.isfile(filepath) and os.stat(filepath).st_size != 0:
        loadfile = open(filepath, 'rb')

        global registeredUsers
        registeredUsers = pickle.load(loadfile)

        loadfile.close()

        print("Here's all the registered user we just loaded")
        [print(user.accountNum) for user in registeredUsers] #TODO get rid of this

def saveRegisteredUsers():
    saveFile = open(app.config["REGISTERED_USERS_SAVE"], 'wb')
    pickle.dump(registeredUsers, saveFile)
    saveFile.close()

def validateUser(accountNum, password):
    """Checks if the imported customer and password match a user of the website. 
    If so, returns the relevant user object. Returns 'None' otherwise."""
    
    print("DEBUG: Here's all the users")
    [print(user.accountNum) for user in registeredUsers] #TODO get rid of this

    foundUser = None

    for user in registeredUsers:
        if user.accountNum == accountNum and user.password == password:
            foundUser = user
            break

    return foundUser

def findUser(accountNum):
    print(f"DEBUG: Searching for account {accountNum}")
    print("DEBUG: Here's all the users")
    [print(user.accountNum) for user in registeredUsers] #TODO get rid of this

    for user in registeredUsers:
        if user.accountNum == accountNum:
            print("User found!")
            return user
    
    return None

def generateAccountNum(min=1000, max=9999):
    """Generates a random account number that does not match that of any other registered user."""
    accountNum = random.randint(min, max)
    while accountNum in [user.accountNum for user in registeredUsers]:
        accountNum = random.randint(min, max)
    
    return accountNum

################
### SESSIONS ###
################
# All the adding/removing for sessions must be handled externally to this dictionary

sessions = {} # KEY: Session ID | VALUE: Session Object

# RETRIEVED FROM https://pynative.com/python-generate-random-string/
def get_random_string(length):
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string is:", result_str)
    return result_str

def generateSessionID():
    # Generate a random session ID
    randomID = get_random_string(8)
    while randomID in sessions:
        randomID = get_random_string(8)

    return randomID

def createUserSession(session, user):
    """Associates the imported session with the imported user."""
    global sessions
    if not session["SESSION_ID"] in sessions:
        raise ValueError("Session does not exist!")
    
    print(f"Creating user session between ID {session['SESSION_ID']} and user {user.accountNum}")

    sessions[session["SESSION_ID"]].accountNum = user.accountNum

    saveSessions()

def manageSession(session, urlSessionID):
    """Manages the session process - if the imported session has not been given an id (and no ID is provided in the url), then it is provided one.
        If the session ID given is not yet in the list of active sessions, it is added. This method is insecure by design."""
    loadSessions()
    
    print("In manage session - here's all the sessions:")
    for s in sessions:
        sessionObj = sessions[s]
        print(f"{sessionObj.ID}: {sessionObj.accountNum}")
    
    # Make URL session ID override the existing session
    if urlSessionID is not None: # If the url specifies a session ID
        print("ENTERED URL SESSION ID")
        session["SESSION_ID"] = urlSessionID
    else:
        if session.get("SESSION_ID") is None: # If there is no session ID in the url or cookie
            # Generate a random new Session ID
            session["SESSION_ID"] = generateSessionID()
        else:
            print(f"Session ID WAS in session, was {session['SESSION_ID']}") #TODO remove me
    print(f"Managing session, new session ID is {session['SESSION_ID']}")

    # Now that we assure the user has a session ID, add it to the list of sessions if not already there.
    if session["SESSION_ID"] not in sessions:
        sessions[session["SESSION_ID"]] = Session(session["SESSION_ID"], None)
    
    saveSessions()

def validateSession(session):
    """Validates if the imported session is associated with a user."""
    loadSessions()

    if not session["SESSION_ID"] in sessions:
        raise ValueError("Session does not exist!")
    
    # Check if session ID has an associated account that is logged in
    if sessions[session["SESSION_ID"]].accountNum is not None:
        return True
    else:
        return False

def loadSessions():
    filepath = app.config["SESSIONS_SAVE"]
    if os.path.isfile(filepath) and os.stat(filepath).st_size != 0:
        loadfile = open(filepath, 'rb')

        global sessions
        sessions = pickle.load(loadfile)

        loadfile.close()

def saveSessions():
    saveFile = open(app.config["SESSIONS_SAVE"], 'wb')
    pickle.dump(sessions, saveFile)
    saveFile.close()



###########################
### METHODS FOR TESTING ###
###########################

def reinitialise():
    """Renitialises the global state (useful for testing)"""
    global registeredUsers, sessions

    registeredUsers = []
    sessions = {}
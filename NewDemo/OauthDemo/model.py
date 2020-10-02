
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

def addRegisteredUser(user):
    """Adds the imported user to the list of users"""
    registeredUsers.append(user)

    print("Just added a registered user: Here's all the users")
    [print(user.accountNum) for user in registeredUsers]


def loadRegisteredUsers():
    filepath = app.config["REGISTERED_USERS_SAVE"]
    if os.path.isfile(filepath) and os.stat(filepath).st_size != 0:
        loadfile = open(filepath, 'rb')

        global registeredUsers
        registeredUsers = pickle.load(loadfile)

        loadfile.close()

def saveRegisteredUsers():
    saveFile = open(app.config["REGISTERED_USERS_SAVE"], 'wb')
    pickle.dump(registeredUsers, saveFile)
    saveFile.close()

def validateUser(accountNum, password):
    """Checks if the imported customer and password match a user of the website. 
    If so, returns the relevant user object. Returns 'None' otherwise."""
    
    foundUser = None

    for user in registeredUsers:
        if user.accountNum == accountNum and user.password == password:
            foundUser = user
            break

    return foundUser

def findUser(accountNum):
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

def createSession(user):
    """Create a session object for the imported user. Returns the session ID of the created session. 
        ACTUAL SESSION MANAGEMENT IS NOT THE RESPONSIBILITY OF THIS METHOD."""

    # Generate a random session ID
    randomID = get_random_string(8)
    while randomID in sessions:
        randomID = get_random_string(8)
        print(sessions)

    print(f"Creating new session with ID {randomID} and user account Num {user.accountNum}")

    # Create the new session and add it to the session dict
    newSession = Session(randomID, user.accountNum)
    sessions[randomID] = newSession

    return newSession

def validateSession(session):
    print("In validate session - here's all the sessions:")
    print(sessions)
    for s in sessions:
        sessionObj = sessions[s]
        print(f"{sessionObj.ID}: {sessionObj.accountNum}")
    
    """Checks whether the imported session has a session object and whether that session object is still validated (i.e. in the dict of session objects)"""
    if "SESSION_ID" in session:
        if session["SESSION_ID"] in sessions:
            return True
    
    return False

def invalidateSession(sessionID):
    """Invalidates the session object with the imported session ID. Does NOT remove the actual session."""
    sessions.pop(sessionID)


###########################
### METHODS FOR TESTING ###
###########################

def reinitialise():
    """Renitialises the global state (useful for testing)"""
    global registeredUsers, sessions

    registeredUsers = []
    sessions = {}
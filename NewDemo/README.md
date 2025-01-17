# CCSEP Assignment - OAuth Session Fixation
### Vulnerable Branch

This application demonstrates the Oauth Session Fixation vulnerability in a simulation of a banking application. 

## Program description
The program simulates a banking application (Steve from IT Banking) in which users may register for bank accounts and and deposit/withdraw money. Users are tracked accross different pages of the application using a 'session', which associates an identifier with each active user. Users can choose to log in by creating an account or via a third-party application, either Twitter or Steve's Dodgy Oauth Provider(tm). Logging in this way will utilise the OAuth 1.0 to authorise Steve From IT Banking to user the provider's login credentials to manage a session.

## Running The Application
To follow these instructions, make sure you have Docker installed on your system.

1. Run `make` on the terminal to create the docker image.
2. Run `make run` to start the server.
3. Now you can go on browser and goto localhost:8000 and page will show.

NOTE: In the makefile you can change the host port to whatever you want.
   Alternative commands for building & running dockerized app:
   1. `docker build --rm --tag="whatevername"`
   2. `docker run -p 0.0.0.0:"whatever_host_port":"docker_port"/tcp -it --rm "whatevername"`

Alternatively, the application can be run locally by enabling the same environment variables as those setup in the Dockerfile and installing all requirements within `requirements.txt`, then navigating to the `OauthDemo/` directory and running `sh boot.sh`, while simultaneously running the `sh boot.sh` under `steves_dodgy_oauth_provider/`.

## Testing the Application
A test file that tests for program functionality can be found under `OauthDemo/test_main.py` (and `steves_dodgy_oauth_provider/test_oauth.py` for the custom OAuth provider). This file uses the Pytest library for testing.

To test the file, first run the application (with or without a container), then navigate to the `OauthDemo/` directory and execute the `pytest` command

## Demonstrating The Attack - Step-by-Step Guide
** One example interpretation of OAuth sess fix **
    1. Attacker logs in to twitter auth page but doesn't authorize access yet, instead copies the link.
    2. Attacker sends link to a victim, the victim clicks on the link to page and signs in to authorize.
    3. The following can occur
    	a. Since the victim uses the link indentical to attackers (same auth request code, callback),
	   the attacker can just refresh/goto his auth link to complete auth flow on his end
	   and will be redirected to the victims profile.
	b. The link can also return an access token when auth flow is complete,
	   this token could be used to access whatever part that requires this token
	   
    NOTE: This doesn't work on most oauth (twitter, google, facebook) coz the latest protocol
          have made pratices to mitigate this.

# Steps for conducting OAuth Session Fixation on this web

1. run make && make run - Note: docker containers will be running (1 daemon, other it terminal)
2. Visit http://127.0.0.1:5000/
3. Click to sign in with Dodgy Steve
4. Enter your name
5. If you want exploit oauth session fixation, do not grant access just yet. Observer the browser url and copy the link containing the oauth token.
6. Now you can post this to a victim. (Paste this into another browser and sign in)
7. Now go back to your previous browser refresh your url. You will now have access to the victims account.

NOTES:Clear cache and cookies if browser has bad request or internal errors.

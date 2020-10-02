# CCSEP Assignment - OAuth Session Fixation
### Vulnerable Branch

This application demonstrates a patch to protect against the Oauth Session fixation vulnerability.

## Running The Application
To follow these instructions, make sure you have Docker installed on your system.

1. Run `make` on the terminal to create the docker image.
2. Run `make run` to start the server.
3. Now you can go on browser and go to `localhost:5000` and page will show.

NOTE: In the makefile you can change the host port to whatever you want.
   Alternative commands for building & running dockerized app:
   1. `docker build --rm --tag="whatevername"`
   2. `docker run -p 0.0.0.0:"whatever_host_port":"docker_port"/tcp -it --rm "whatevername"`

Alternatively, the application can be run locally by enabling the same environment variables as those setup in the Dockerfile and installing all requirements within `requirements.txt`, then navigating to the `OauthDemo/` directory and running `sh boot.sh`

## Testing the Application
A test file that tests for program functionality can be found under `OauthDemo/test_main.py`. This file uses the Pytest library for testing.

To test the file, first run the application (with or without a container), then navigate to the `OauthDemo/` directory and execute the `pytest` command
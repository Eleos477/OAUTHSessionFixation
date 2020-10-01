# Docker files don't need to rebuild after every change on code anymore

Follow steps:

    1. If you haven't built yet, run " make " first.
    2. Run " make run " to run the container
    3. If you change code, just exit the docker and run " make run " again
       no need rebuild.
    
    NOTE: one docker container is daemon and you need to run " make stop " to stop it.
       
       
       
       
       
       
If really need to rebuild on every code change and copy code to container on build:

    1. run " make slow "
    2. run " make start "
    3. Every code change run " make slow && make start "

# django-learn

## Introduce
This project I created to learn django and build my own music website.
Here is the demo UI I designed [UI Figma](https://www.figma.com/proto/JIbpwAJY05FgpR7fnjVYKj/Untitled?node-id=4%3A34&starting-point-node-id=1%3A2)

## Set up enviroment
Of course to use django you must have python.
My machine has windows 10 operating system, so the commands I use for cmd
#### Install Django
    pip install django
#### Install Virtualenv
    pip install virtualenv
#### Launch virtual environment
    python -m venv venv
    venv\Scripts\activate
    pip install django (install again to use on virtual)
#### Then we will see (venv) at the top of the command line like this
    (venv) C:\Users\DELL\Desktop\django>
#### Create a project with the name you want
    django-admin startproject name
#### Then we will run it on localhost port 8080
    python manage.py runserver
#### This is the information after you run the command line, copy the https:// link and paste them on google
    Watching for file changes with StatReloader
    Performing system checks...
    
    System check identified no issues (0 silenced).
    August 29, 2022 - 19:36:52
    Django version 4.1, using settings 'lismp3.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
<img src="https://user-images.githubusercontent.com/76780813/187203899-4a783f1a-61b0-461c-ae82-2121dd2c7860.png" width="500">

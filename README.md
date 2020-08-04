                                  # Exam_System
## Description:

Exam_System is a web app.It's main purpose is take exam.

## Installation:

1.First install xamp server.
2.Install radis broker(version 2.10.6)
3.Install virtualenvironment
4.Clone the project in the virtualenvironment
5.Active virtualenvironment
6.To install packages give command in commandline or powershell "pip install -r requirements.txt"

## Run project:

1.Start mysql server
2.Start radis server
3.Open two command prompt or powershell
4.To run celery server "celery -A Exam_System worker --loglevel=info"
5.To run main server "python manage.py runserver"


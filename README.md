# Online Exam System

 A Django based  exam website.

# Requirements (that shall be installed in your system)

1. Git <br> 
2. Python <br>
version 3.6.2 <br>
<code><link> https://www.python.org/downloads/release/python-362/ </code> <br>
3. virtualenv <br>
install command > pip install virtualenv <br>
4. Mysql database <br>
5. Redis server <br>
version 3.0.504 <br>
<code><link> https://github.com/microsoftarchive/redis/releases </code> <br>


# Run On Your Machine?

1. Firstly, clone the repository using the git shell <br>
<code>$ git clone https://github.com/AshikurRahman-sec/Exam_System</code> <br>
2. Create a virtual environment and activate it. <br>
<code>$ virtualenv venv</code> <br>
<code>$ venv\Scripts\activate</code> on Windows or <code>$ source venv/bin/activate</code> on Posix system <br>
3. Goto the base directory of the project <br>
<code>cd exam_system </code> <br>
4. Install the requirements for the project <br>
<code>$ pip install -r requirements.txt</code>  <br>
5. Now start the localhost server<br>
<code>$ python manage.py runserver</code> <br>
5. Now start the Celery server<br>
<code>$ celery -A Exam_System worker -l info</code> <br>

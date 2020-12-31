# How to run

## Install python and create virtual environment 
1. `pt install python3.6`

2. `pip3 install virtualenv`

3. `virtualenv -p python3 env3`

4. `source env3/bin/activate`

5. `cd ml_api`

6. `pip install -r requirements.txt`

## Make migrations and start the server
1. `cd ml_api`

2. `python manage.py makemigrations`

3. `python manage.py makemigrations api`

4. `python manage.py migrate`

5. `python manage.py runserver`

Tasks api should be available at
`http://localhost:8000/api/optimization/tasks/`


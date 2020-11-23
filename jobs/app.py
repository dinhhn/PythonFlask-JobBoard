# import the Flask class and the render_template function from flask
from flask import Flask, g
from flask import render_template
import sqlite3

PATH = "db/jobs.sqlite"

# create an instance of the Flask class called app. Pass the special variable __name__ to the Flask class constructor.
app = Flask(__name__)

# Attach a route() decorator with the URL of / to the jobs function.
@app.route('/')
# Attach an additional route decorator of /jobs.
@app.route('/jobs')
# Note: The jobs function can now be reached at / and /jobs

# Create a basic route in app.py by creating a function called jobs.
def jobs():
    jobs = execute_sql('SELECT job.id, job.title, job.description, job.salary, employer.id as employer_id, employer.name as employer_name FROM job JOIN employer ON employer.id = job.employer_id')
    # In the body of the function return a call to the render_template() function, pass a parameter of 'index.html'.
    return render_template('index.html', jobs=jobs)

def open_connection():
    connection = getattr(g, '_connection', None)
    if connection == None:
        connection = sqlite3.connect(PATH)
        g._connection = connection
    connection.row_factory = sqlite3.Row
    return connection

def execute_sql(sql, values = (), commit = False, single = False):
    connection = open_connection()
    cursor = connection.execute(sql, values)
    if commit == True:
        results = connection.commit()
    else:
        results = cursor.fetchone() if single else cursor.fetchall()
    cursor.close()
    return results

@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_connection', None)
    if connection != None:
        connection.close()
    



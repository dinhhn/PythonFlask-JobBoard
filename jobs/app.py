# import the Flask class and the render_template function from flask
from flask import Flask
from flask import render_template

# create an instance of the Flask class called app. Pass the special variable __name__ to the Flask class constructor.
app = Flask(__name__)

# Attach a route() decorator with the URL of / to the jobs function.
@app.route('/')
# Attach an additional route decorator of /jobs.
@app.route('/jobs')
# Note: The jobs function can now be reached at / and /jobs

# Create a basic route in app.py by creating a function called jobs.
def jobs():
    # In the body of the function return a call to the render_template() function, pass a parameter of 'index.html'.
    return render_template('index.html')


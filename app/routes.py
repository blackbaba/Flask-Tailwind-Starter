import os, sys
import datetime as dt
from flask import (
    render_template,
    url_for,
    redirect,
    request,
    make_response,
    abort,
    jsonify,
    session,
    flash)
from app import app
from app.helpers import *
from app.forms import *
from app.models import *

# Secret key required for sessions and other security purposes
# Use python -c 'import os; print(os.urandom(16))' to generate a secret key

# Home route
@app.route('/')
def index():
    # resp = make_response(render_template(...))
    # resp.set_cookie('username', 'the username')
    name = "Test User"
    flash('Welcome to home page') # Flash messages
    # flash('Welcome to home page', 'error') # Flash messages with categories
    return render_template('index.html', name = name), 200 # returning status code with response

# Accessing Request data
@app.route('/request_data', methods=['POST', 'GET'])
def request_data():
    error = None
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            searchword = request.args.get('key') # Returns none if key not present
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('index.html', error=error)


# url_for helper function demonstration
@app.route('/url_helper', methods=['GET', 'POST'])
def url_helper():
    return f"{url_for('index')} is root url and {url_for('static', filename='dist/css/main.css')} is url for the main css file"

# Route with a variable
@app.route('/user/<string:username>/posts/<int:post_id>')
def user_posts(username, post_id):
    return f"Post {post_id} for user {username}"

@app.route('/system')
def system():
    return f"NODE ENV: {os.environ.get('NODE_ENV')},  FLASK ENV: {os.environ.get('FLASK_ENV')} and Configuration profile for: {app.config.get('TEST_CONFIG')}"

# Accessing query params
@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int) # function sets a default value as well as casts to int
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

# Dict is automatically JSONified in responses
@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }

@app.route("/users")
def users_api():
    users = get_all_users()
    return jsonify([user.to_json() for user in users])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return render_template('index.html', name=session['username'])
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# Example of an error handler
@app.errorhandler(404)
def resource_not_found(e):
    # return render_template('404.html'), 404
    return jsonify(error=str(e)), 404

@app.route("/cheese")
def get_one_cheese():
    resource = get_resource()

    if resource is None:
        abort(404, description="Resource not found")

    return jsonify(resource)
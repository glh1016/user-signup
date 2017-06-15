from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def display_home():
    return render_template('index-home.html')


def is_field_empty(field):
    if field = ""
    return True

def password_invalid(password):
    if password.isalpha

#def password_mismatch():
#def valid_email():







@app.route("/", methods = ['POST'])
def validate_form():
    return validate_form.format

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']




@app.route("/welcome", methods=['POST'])
def hello():
    first_name = request.form['username']
    return render_template('welcome.html', name=username)




#The user leaves any of the following fields empty: username, password, verify password.


#The user's username or password is not valid -- for example, it contains a space character or it consists of less than 3 characters or more than 20 characters (e.g., a username or password of "me" would be invalid).


#The user's password and password-confirmation do not match.


#The user provides an email, but it's not a valid email. Note: the email field may be left empty, but if there is content in it, then it must be validated. The criteria for a valid email address in this assignment are that it has a single @, a single ., contains no spaces, and is between 3 and 20 characters long.



    
#If the user's form submission is not valid, you should reject it and re-render the form with some feedback to inform the user of what they did wrong. The following things should trigger an error:
  
#Each feedback message should be next to the field that it refers to.

#For the username and email fields, you should preserve what the user typed, so they don't have to retype it. With the password fields, you should clear them, for security reasons.

#If all the input is valid, then you should redirect the user to a welcome page that uses the username input to display a welcome message of: "Welcome, [username]!"

###Use templates (one for the index/home page and one for the welcome page) to render the HTML for your web app.

app.run()
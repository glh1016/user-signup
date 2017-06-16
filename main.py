from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def display_home():
    return render_template('index-home.html',username='',password='',verify='',email='')


def is_field_empty(field):
    if field == "":
        return True
    else:
        return False

def correct_length(field):
    if len(field)>2 and len(field)<20:
        return True
    else:
        return False

def email_parts(field):
    if ('@' in field) and ('.' in field):
        return True
    else:
        return False



@app.route("/", methods = ['POST'])
def validate_form():
    

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    #valid username

    if is_field_empty(username):
         username_error = "Empty field"
         username = ''
    else: 
        username = username
        if username.isalpha() and correct_length(username):
            username = username
        else:
            username_error = 'Invalid username'
            username = username   
         
    
    #valid password
    
    if is_field_empty(password):
        password_error = "Empty field"
        password = ''
    else:
        password = password
        if password.isalpha() and correct_length(password):
            password=password
        else:
            password_error = "Invalid password"
            password = password
    
    
    
    # do passwords match 
    
    if is_field_empty(verify):
        verify_error = "Empty field"
        verify = ''
    else:
        verify = verify
        if verify != password:
            verify_error = 'Passwords do not match'
            password_error = 'Passwords do not match'
            password = ''
            verify = ''
    
    #email validation syntax
    if is_field_empty(email):
        email_error = ''
        email = ''
    else:
        email = email
        if correct_length(email) and email_parts(email):
            email = email
        else: 
            email_error = 'Invalid email'
            email = email

    
    
    if not username_error and not password_error and not verify_error and not email_error: 
        return redirect('/welcome')
    else:
        return render_template('index-home.html',username_error=username_error,password_error=password_error,verify_error=verify_error,username=username,password=password,verify=verify,email=email,email_error=email_error)

    



@app.route('/welcome')
def welcome():
    #username = request.form['username']
    return render_template('welcome.html',username = '')
    #return '<h1> Welcome! </h1>'

app.run()




##The user leaves any of the following fields empty: username, password, verify password.


##The user's username or password is not valid -- for example, it contains a space character or it consists of less than 3 characters or more than 20 characters (e.g., a username or password of "me" would be invalid).


##The user's password and password-confirmation do not match.


##The user provides an email, but it's not a valid email. Note: the email field may be left empty, but if there is content in it, then it must be validated. The criteria for a valid email address in this assignment are that it has a single @, a single ., contains no spaces, and is between 3 and 20 characters long.


##If the user's form submission is not valid, you should reject it and re-render the form with some feedback to inform the user of what they did wrong. The following things should trigger an error:
  
##Each feedback message should be next to the field that it refers to.

##For the username and email fields, you should preserve what the user typed, so they don't have to retype it. With the password fields, you should clear them, for security reasons.

##If all the input is valid, then you should redirect the user to a welcome page that uses the username input to display a welcome message of: "Welcome, [username]!"

#Use templates (one for the index/home page and one for the welcome page) to render the HTML for your web app.


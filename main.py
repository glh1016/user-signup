from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('index-home.html')
    return template.render()


@app.route("/welcome", methods=['POST'])
def hello():
    first_name = request.form['username']
    template = jinja_env.get_template('welcome.html')
return template.render(name=username)


form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            .error {{
                color: red;
            }}
        </style>
    </head>
    <body>
    <h1>Signup</h1>
        <form method="post">
            <table>
                <tr>
                    <td><label for="username">Username</label></td>
                    <td>
                        <input name="username" type="text" value='{username}'>
                        <span class="error">{username_error}</span>
                    </td>
                </tr>
                <tr>
                    <td><label for="password">Password</label></td>
                    <td>
                        <input name="password" type="password" value='{password}'>
                        <span class="error">{password_error}</span>
                    </td>
                </tr>
                <tr>
                    <td><label for="verify">Verify Password</label></td>
                    <td>
                        <input name="verify" type="password" value='{verify}'>
                        <span class="error">{verify_error}</span>
                    </td>
                </tr>
                <tr>
                    <td><label for="email">Email (optional)</label></td>
                    <td>
                        <input name="email" type="email" value='{email}'>
                        <span class="error">{email_error}</span>
                    </td>
                </tr>
            </table>
            <input type="submit">
        </form>
    </body>
</html>"""

@app.route("/")
def display_form():
    return form.format(username='',username_error='',password='',password_error='',verify='',verify_error='',email='', email_error='')

#The user leaves any of the following fields empty: username, password, verify password.
def field_empty():

#The user's username or password is not valid -- for example, it contains a space character or it consists of less than 3 characters or more than 20 characters (e.g., a username or password of "me" would be invalid).
def password_invalid():

#The user's password and password-confirmation do not match.
def password_mismatch():

#The user provides an email, but it's not a valid email. Note: the email field may be left empty, but if there is content in it, then it must be validated. The criteria for a valid email address in this assignment are that it has a single @, a single ., contains no spaces, and is between 3 and 20 characters long.
def valid_email():


@app.route("/validate-form", methods = ['POST'])
def validate_form():
    return validate_form.format

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

#If the user's form submission is not valid, you should reject it and re-render the form with some feedback to inform the user of what they did wrong. The following things should trigger an error:

        #The user leaves any of the following fields empty: username, password, verify password.

        #The user's username or password is not valid -- for example, it contains a space character or it consists of less than 3 characters or more than 20 characters (e.g., a username or password of "me" would be invalid).

        #The user's password and password-confirmation do not match.

        #The user provides an email, but it's not a valid email. Note: the email field may be left empty, but if there is content in it, then it must be validated. The criteria for a valid email address in this assignment are that it has a single @, a single ., contains no spaces, and is between 3 and 20 characters long.
    
#Each feedback message should be next to the field that it refers to.

#For the username and email fields, you should preserve what the user typed, so they don't have to retype it. With the password fields, you should clear them, for security reasons.

#If all the input is valid, then you should redirect the user to a welcome page that uses the username input to display a welcome message of: "Welcome, [username]!"

#Use templates (one for the index/home page and one for the welcome page) to render the HTML for your web app.

app.run()
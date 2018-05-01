from flask import Flask, request, redirect, render_template
import cgi
import os
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/signup", methods=['POST'])
def signup():
    username = request.form['username']
    username_error = ""
    user_password = request.form['password']
    user_password_error = ""
    validate_password = request.form['verify']
    validate_password_error = ""
    user_email = request.form['email']
    user_email_error = ""

#Validate Username
    if username == "":
        username_error = "To proceed, please enter a valid username."
    elif len(username) <= 3 or len(username) > 20:
        username_error = "Please choose a username between 3 and 20 characters."
        username = ""
    elif " " in username:
        username_error = "Please enter a username without spaces."
        username = ""

#validate User's Password
    if user_password == "":
        user_password_error = "To proceed, please enter a valid password."
    elif len(user_password) <= 3 or len(user_password) > 20:
        user_password_error = "Passwords must be between 3 and 20 characters, please correct to proceed."
        username = ""
    elif " " in user_password:
        user_password_error = "Passwords can not contain spaces."

    if validate_password == "" or verify != password:
        validate_password_error = "Your passwords do not match, please re-enter."

    
 #validate User's Email
    if user_email != "": #only validate if entered, can optionally be left blank
        user_password_error = "To proceed, please enter a valid password"
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            email_error = "This is not a valid email address, please correct, OR - choose the option of leaving blank"

#If no errors, return welcome message
        if not username_error and not user_password_error and not _validate_password_error and not user_email_error:
            return render_template('welcome.html', username = username)

#If errors, return form with username and email (if entered), but excluding password entries
    else:
        return render_template('index.html', 
        username = username,  #username can be left intact so that user does not have to re-enter 
        username_error = username_error, 
        user_password_error = user_password_error, 
        validate_password_error = validate_password_error, 
        email = email, #email can be left intact so that user does not have to re-enter
        email_error = email_error)


    
app.run()
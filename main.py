from flask import Flask, request, redirect, render_template, url_for
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
    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""    

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
    if password == "":
        password_error = "To proceed, please enter a valid password."
    elif len(password) <= 3 or len(password) > 20:
        password_error = "Passwords must be between 3 and 20 characters, please correct to proceed."
        
    elif " " in password:
        password_error = "Passwords can not contain spaces."

    if verify == "" or verify != password:
        verify_error = "Your passwords do not match, please re-enter."
        verify = ""

    
 #validate User's Email
    if email != "": #only validate if entered, can optionally be left blank
        user_error = "To proceed, please enter a valid password"
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            email_error = "This is not a valid email address, please correct, OR - choose the option of leaving blank"

#If no errors, return welcome message
        if not username_error and not password_error and not verify_error and not email_error:
            username = username
            return render_template('welcome.html', username=username)

#If errors, return form with username and email (if entered), but excluding password entries
        else:
            return render_template('index.html', 
            username = username, #can be left intact so that user does not have to re-enter
            username_error = username_error, 
            password_error = password_error,
            verify_error = verify_error,
            email = email, #can be left intact so that user does not have to re-enter
            email_error = email_error)

@app.route('/welcome')
def complete_signup():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)


    
app.run()
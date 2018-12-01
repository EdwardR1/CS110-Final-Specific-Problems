# Connected with Object Oriented Programming Question
# Create a Website with a form asking for a name of a class and grade
# Upon submitting the form, in the form redirect, create a new Subject Object and read the string method (__str__ method), showing on the screen the class name and grade associated.
# Extension:
    # Create a list of Subjects and allow User to keep adding to the list by pressing back
        # Think of the ToDo List Lab question

from oop import Subject
from flask import Flask, request
app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    pass


@app.route('/form_input')
def input():
    pass



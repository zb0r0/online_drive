from flask import Flask, render_template, redirect, session, request
import os, filetype
import sqlalchemy

app = Flask(__name__)



@app.route('/')
def home_page():  # put application's code here
    return render_template("index.html")


if __name__ == '__main__':
    app.run()

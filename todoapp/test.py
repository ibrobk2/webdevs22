from flask import Flask, render_template, redirect, url_for


test = Flask(__name__)

@test.route('/register')
def register():
    return render_template("register.html")

@test.route('/login')
def login():
    return render_template("login.html")


@test.route('/')
def index():
    return render_template("test.html")

if __name__ == '__main__':
    test.run('127.0.0.1', 4000)
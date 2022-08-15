from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "This is Homepage"


@app.route('/michael')
def index():
    return render_template('test.html')


if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port='7000', debug = True)
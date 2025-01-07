from flask import Flask

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome to Flask framework'

@app.route('/guys')
def welcome1():
    return 'Welcome to Flask framework guys'

if __name__ == '__main__':
    app.run(debug = True)
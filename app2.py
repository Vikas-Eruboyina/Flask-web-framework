## building URL dynamically in flask framework

from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return '<html><body><a href="/results/21">Welcome to student results</a></html></body>'

@app.route('/pass/<int:score>')
def passed(score):
    return "<html><body><h2>The person is Passed</h2></body> </html>"

@app.route('/fail/<int:score>')
def fail(score):
    return "<html><body><h2>The person is Failed</h2></body> </html>"


## result checker      
@app.route('/results/<int:marks>')
def results(marks):
    result=''
    if marks < 35:
        result= "fail"
    else:
        result= "passed"

    return redirect(url_for(result,score = marks))


if __name__ == '__main__':
    app.run(debug = True)
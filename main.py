## Integrating HTML with flask #Jinja2 technique
# HTTP verb GET and POST
from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/results/<int:score>')
def results(score):
    res = ''
    if score >= 35:
        res = "Pass with score {}".format(score)
    else:
        res = "Fail with score {}".format(score)

    return render_template('results.html',result = res)

## result checker HTML page
@app.route('/submit',methods=['POST','GET'])

def submit():
    total_score = 0
    if request.method == "POST":
        science = float(request.form['science'])
        maths   = float(request.form['maths'])
        C       = float(request.form['c'])
        datascience = float(request.form['datascience'])
        total_score= (science+maths+C+datascience)/4

    return redirect(url_for('results',score = total_score))


if __name__ == '__main__':
    app.run(debug = True)
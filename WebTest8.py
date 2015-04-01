from flask import Flask,render_template,request,url_for
from test import dataCreate
import sql_str

app = Flask(__name__)
timeline = []

@app.route('/')
def hello_world():
    cururl=url_for('hello_world')
    return render_template("openform.html",mainurl=cururl)

@app.route('/msearch&<count>',methods=['POST'])
def msearch(count):
    i=0
    j=0
    ct=count
    time = []
    tupletime = []
    while i <= int(ct):
        time.append(request.form.get('start'+str(i)).encode('utf-8'))
        time.append(request.form.get('end'+str(i)).encode('utf-8'))
        i=i+1
    sortedtime=sorted(time)
    print sortedtime
    while j <= int(ct)*2:
        a=(sortedtime[j],sortedtime[j+1])
        tupletime.append(a)
        j=j+2
    timeline=tupletime
    testdata=dataCreate(timeline)
    return render_template('result.html',testdata=testdata)


@app.route('/result.html')
def result():
    testdata=dataCreate(timeline)
    return render_template('result.html',testdata=testdata)

@app.route('/result1.html')
def result1():
    testdata=dataCreate(timeline)
    return render_template('result1.html',testdata=testdata)


if __name__ == '__main__':
    app.run("0.0.0.0",debug=True)

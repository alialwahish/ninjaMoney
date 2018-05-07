from flask import Flask, render_template,redirect,request,session
import datetime
import random


app = Flask(__name__)
app.secret_key="myKey"
lst=[]
@app.route('/')
def index():
    global lst
    lst=[]
    session['gold']=0
    session['times']=""
    session['events']=[]
    
    return render_template("index.html")

@app.route('/process_money',methods=["POST"])
def process_money():
    global lst
    if request.form['building'] == "farm":
        session['building']="Farm"
        print request.form['building']
        session['amount']=random.randrange(10,20)
        
        print session['amount']
        session['gold']+=session['amount']


    elif request.form['building'] == "Cave":
        session['building']="Cave"
        session['amount']=random.randrange(4,11)
        session['gold']+=int(session['amount'])
        

    elif request.form['building'] == "House":
        session['building']="House"
        session['amount']=random.randrange(1,6)
        session['gold']+=int(session['amount'])
       

    elif request.form['building'] == "Casino":
        session['building']="Casino"
        print request.form['building']
      
        session['amount']=random.randrange(-51,51)
        session['gold']+=int(session['amount'])

        session['dateNtime']=datetime.datetime.now()
        lst.append([session['building'],session['amount'],session['dateNtime']])
        session['events']=lst
        
        if int(session['gold']<0):
            print "less than zero"
            session['gold']=0

        print "total Gold: ",session['gold']
        return render_template('index.html')        
   
    print "total Gold: ",session['gold']
    session['dateNtime']=datetime.datetime.now()
    lst.append([session['building'],session['amount'],session    ['dateNtime']])
    session['events']=lst
    return render_template('index.html')

app.run(debug=True)
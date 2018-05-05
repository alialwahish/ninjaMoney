from flask import Flask, render_template,redirect,request,session
import random
app = Flask(__name__)
app.secret_key="myKey"

@app.route('/')
def index():
    session['gold']=0
    session['actMes']=""
    session['events']=[]
    return render_template("index.html")

@app.route('/process_money',methods=["POST"])
def process_money():
    
    if request.form['building'] == "farm":
        
        print request.form['building']
        session['amount']=random.randrange(10,20)
        
        print session['amount']
        session['gold']+=session['amount']


    elif request.form['building'] == "Cave":
        session['amount']=random.randrange(4,11)
        session['gold']+=int(session['amount'])
        

    elif request.form['building'] == "House":
        session['amount']=random.randrange(1,6)
        session['gold']+=int(session['amount'])
       

    elif request.form['building'] == "Casino":
        print request.form['building']
        tog =random.randrange(0,2)==1
        print tog
        if tog == 1:
            session['amount']=random.randrange(0,50)
            session['gold']+=int(session['amount'])
            
            session['actMes']="Entered a "+request.form['building']+" and won "+str(session['amount'])+" golds... Yey.."


        else:
            session['amount']=random.randrange(0,51)
            session['gold']-=int(session['amount'])
            session['actMes']= "Entered a "+request.form['building']+" and lost "+str(session['amount'])+" golds... Ouch.."
            print "total Gold: ",session['gold']



            if int(session['gold']<0):
                print "less than zero"
                session['gold']=0

        msg = session['actMes']
        print msg
        msg=msg
        print "total Gold: ",session['gold']
        return render_template('index.html',msg=msg)        
    

    session['actMes']="Earned "+str(session['amount'])+" golds from the "+request.form['building']+"!"
    msg = session['actMes']
    msg=msg
        
    print msg
    
    print "total Gold: ",session['gold']

    return render_template('index.html',msg=msg)

app.run(debug=True)
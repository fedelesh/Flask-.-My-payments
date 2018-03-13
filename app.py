from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///pay.db'
db = SQLAlchemy(app)
abc=''

class Pay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer)
    text=db.Column(db.String(200))
    money=db.Column(db.Integer)

@app.route('/')
def index():
    pays = Pay.query.all()
    return render_template('index.html', pays=pays)

@app.route('/add', methods=['POST'])
def add():
    pay = Pay(text=request.form['reason'],money=request.form['money'],date=request.form['date'])
    if pay.money!='':
        db.session.add(pay)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/clear', methods = ['GET', 'POST'])
def clear():
        pays = Pay.query.all()
        Pay.query.delete()
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/df',methods=['POST','GET'])
def df():
        pays = Pay.query.all()
        abc=request.form['inp']
        su=0
        pays2 = Pay.query.filter_by(date=abc).all()

        for i in pays2:
            if i.money!='':
                su+=i.money
            else:
                su+=0

        return render_template('index.html', pays2=pays2, pays=pays, su=su)


if __name__=="__main__":
   app.run(debug = True)

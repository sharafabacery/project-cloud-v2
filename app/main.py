from typing import Text
import json
from flask import Flask, request, render_template

app = Flask(__name__)

# postgresql://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hello_flask:hello_flask@db:5432/hello_flask_dev'

from models import db, Student

db.init_app(app)
with app.app_context():
    # To create / use database mentioned in URI
    db.create_all()
    db.session.commit()
    print("fffffffffff")

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/savedata',methods=['POST'])
def savedata():
    ID=request.form['ID']
    username=request.form['username']
    GPA=request.form['GPA']
    Link_Image=request.form['Link_Image']
    print('test1')
    record=Student(ID=ID,username=username,GPA=GPA,linkImage=Link_Image)
    print("Text2")
    db.session.add(record)
    print("Text3")
    db.session.commit()
    print("text4")
    return render_template('index.html')
@app.route('/students',methods=['GET','POST'])
def getStudents():
    list=[]
    Students = Student.query.all()
    for st in Students:
        list.append({'username':st.username,"ID":st.ID,"GPA":st.GPA,"linkImage":st.linkImage})
    return json.dumps(list)

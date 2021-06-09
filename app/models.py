from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    ID = db.Column(db.String, primary_key=True)
    username = db.Column(db.String)
    GPA = db.Column(db.String)
    linkImage = db.Column(db.String)

    def __init__(self, ID, username, GPA, linkImage):
        self.ID = ID
        self.username = username
        self.GPA = GPA
        self.linkImage = linkImage

    def __repr__(self):
        return f'<User-username-GPA-image : {self.ID}-{self.username}-{self.GPA}-{self.linkImage}'

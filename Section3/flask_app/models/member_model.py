from flask_app import db

class Member(db.Model):
    __tablename__ = "member"

    id = db.Column(db.Integer(), primary_key=True)
    gender = db.Column(db.Integer())
    age = db.Column(db.Integer())
    wpi_id = db.Column(db.Integer(), db.ForeignKey('wpi.id'))
    wpi = db.relationship('Wpi', backref='member')
    
    def __repr__(self):
        return f"<Member id: {self.id}, gender: {self.gender}, age: {self.age}>"
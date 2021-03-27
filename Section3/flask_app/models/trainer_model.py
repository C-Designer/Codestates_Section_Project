from flask_app import db

class Trainer(db.Model):
    __tablename__ = 'trainer'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    sex = db.Column(db.Integer())
    age = db.Column(db.Integer())
    wpi_id = db.Column(db.Integer(), db.ForeignKey('wpi.id'))
    wpi = db.relationship('Wpi', backref='trainer')

    def __repr__(self):
        return f"<Trainer id:{self.id} name:{self.name}>"
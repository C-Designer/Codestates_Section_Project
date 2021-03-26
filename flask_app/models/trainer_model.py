from flask_app import db

class Trainer(db.Model):
    __tablename__ = 'trainer'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())

    def __repr__(self):
        return f"<Trainer id:{self.id} name:{self.name}>"
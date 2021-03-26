from flask_app import db

class Sale(db.Model):
    __tablename__ = "sale"

    id = db.Column(db.Integer(), primary_key=True)
    is_sale = db.Column(db.Integer(), nullable=False)
    type = db.Column(db.String(), default='miss')
    member_id = db.Column(db.Integer(), df.ForeignKey('member.id'), nullable=False)
    trainer_id = db.Column(db.Integer(), df.ForeignKey('trainer.id'), nullable=False)

    member = db.relationship('Member', backref='sale')
    trainer = db.relationship('Trainer', backref='sale')

    def __repr__(self):
        return f"<Sale id:{self.id}, is_sale:{self.is_sale}, type:{self.type}>"
from flask_app import db

class Wpi(db.Model):
    __tablename__ = 'wpi'

    id = db.Column(db.Integer(), primary_key=True)
    
    real = db.Column(db.Integer(), nullable= False)
    roman = db.Column(db.Integer(), nullable= False)
    human = db.Column(db.Integer(), nullable= False)
    ideal = db.Column(db.Integer(), nullable= False)
    agent = db.Column(db.Integer(), nullable= False)

    relation = db.Column(db.Integer(), nullable= False)
    trust = db.Column(db.Integer(), nullable= False)
    manual = db.Column(db.Integer(), nullable= False)
    self = db.Column(db.Integer(), nullable= False)
    culture = db.Column(db.Integer(), nullable= False)

    def __repr__(self):
        return  str([self.id
                , self.real
                , self.roman
                , self.human
                , self.ideal
                , self.agent
                , self.relation
                , self.trust
                , self.self
                , self.culture])
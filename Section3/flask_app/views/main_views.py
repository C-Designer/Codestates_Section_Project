from flask import Blueprint, render_template
from flask_app.models.wpi_model import Wpi
from flask_app.models.trainer_model import Trainer
from flask_app.models.member_model import Member
from flask_app.models.sale_model import Sale

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():

    Trainer.query.all()
    Wpi.query.all()
    Member.query.all()
    Sale.query.all()
    
    return render_template('index.html'), 200
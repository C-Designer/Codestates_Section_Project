from flask import Blueprint, render_template
from flask_app.models.trainer_model import Trainer

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():

    trainer_list = Trainer.query.all()
    return render_template('index.html', trainer_list=trainer_list), 200
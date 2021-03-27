from flask import Blueprint, render_template
from flask_app.models.member_model import Member

member_bp = Blueprint('member', __name__)

@member_bp.route('/')
def view_list():
    member_list = Member.query.all()

    return render_template('member/member_list.html', member_list=member_list), 200
from flask import Blueprint, render_template

bp = Blueprint('member', __name__)

@bp.route('/member', methods=['POST'])
def add_member():

    if request.method =="POST":
        j_son = request.get('name')
        name = j_son.get
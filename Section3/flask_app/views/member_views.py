from flask import Blueprint, render_template, redirect, url_for
from flask.globals import request
from flask_app.models.member_model import Member
from flask_app.models.sale_model import Sale
from flask_app import db

bp = Blueprint('member', __name__)

@bp.route('/member/', methods=['POST'])
def add_member():

    if request.method == "POST":
        try:
            id = int(request.form['id'])
            sex = int(request.form['sex'])
            age = int(request.form['age'])
            
            real = int(request.form['real'])
            roman = int(request.form['roman'])
            human = int(request.form['human'])
            ideal = int(request.form['ideal'])
            agent = int(request.form['agent'])
            
            relation = int(request.form['relation'])
            trust = int(request.form['trust'])
            manual = int(request.form['manual'])
            confidence = int(request.form['confidence'])
            culture = int(request.form['culture'])
        except:
            return "Needs options", 400

        member = Member(id=id, sex=sex, age=age, real=real, roman=roman, human=human, ideal=ideal, agent=agent, relation=relation, trust=trust, manual=manual, confidence=confidence, culture=culture)
        raw_member = Member.query.filter(Member.id == id).first()
        # id를 확인하여 이미 있는 회원인지 확인
        if raw_member:
            db.session.delete(raw_member)
        
        db.session.add(member)
        db.session.commit()
        return redirect(url_for('main.member_index'), code=200)

@bp.route('/member/', defaults={ 'member_id' : None })
@bp.route('/member/<int:member_id>')
def delete_member(member_id):
    # 던진 값이 없을시 404 반환
    if not member_id:
        return 'None', 400

    sales = Sale.query.filter(Sale.member_id == member_id).all()
    if sales:
        for sale in sales:
            db.session.delete(sale)
            db.session.commit()

    # 유저가 db에 없을시 404 반환, 있을시 삭제후 리다이렉트
    member = Member.query.filter(Member.id == member_id).first()
    if not member:
        return 'None', 404
    else:
        db.session.delete(member)
        db.session.commit()

    return redirect(url_for('main.member_index'), code=200)
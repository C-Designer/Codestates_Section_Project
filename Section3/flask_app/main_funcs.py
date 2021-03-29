from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from flask_app.models.sale_model import Sale
from flask_app.models.member_model import Member
from flask_app.models.trainer_model import Trainer

def member_grade_machine(member_num):
    '''
        회원번호 기입시 값을 불러와 난이도 측정
    '''
    members = []
    target = []

    sales = Sale.query.all()
    for sale in sales:
        m = Member.query.filter(Member.id == sale.member_id).first()
        if not members:
            return "데이터 내 회원정보가 없습니다"
        members.append([m.sex, m.age, m.real, m.roman, m.human, m.ideal, m.agent, m.relation, m.trust, m.manual, m.confidence, m.culture])
        target.append(sale.is_sale)
    feature = pd.DataFrame(data=np.array(members), columns=['sex', 'age', 'real', 'roman', 'human', 'ideal', 'agent', 'relation', 'trust', 'manual', 'self', 'culture'])
    
    model = LinearRegression()
    model.fit(feature, target)
    
    m = Member.query.filter(Member.id == member_num).first()
    prediction = model.predict([[[m.sex, m.age, m.real, m.roman, m.human, m.ideal, m.agent, m.relation, m.trust, m.manual, m.confidence, m.culture]]])

    return prediction





def member_grade(m):
    member = [m.sex, m.age, m.real, m.roman, m.human, m.ideal, m.agent, m.relation, m.trust, m.manual, m.confidence, m.culture]


def predict_text(user_list, predict_text):
    user_1, user_2 = user_list

    embeddings = []
    labels = []

    for tw in user_1.tweets:
        embeddings.append(tw.embedding)
        labels.append(user_1.username)

    for tw in user_2.tweets:
        embeddings.append(tw.embedding)
        labels.append(user_2.username)

    classifier = LinearRegression()
    classifier.fit(embeddings, labels)

    predict_embedding = en.encode(texts=[predict_text])
    prediction = classifier.predict(predict_embedding)

    print(f"Prediction Results {prediction[0]}")

    return prediction[0]

import json, os
from flask import Blueprint, request
from models.news import News
from schemas.news import NewsSchema
from services.database import db
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

bp_news = Blueprint('news', __name__, url_prefix='/news')


@bp_news.route('/', methods=['GET'])
def list():
    """
    Lista todas noticias cadastradas
    """    
    try:
        news = News.query.all()
        response = NewsSchema(many=True).dumps(news), 200
    except ValidationError as err:
        response = err.messages, 400
    
    return response

@bp_news.route('/<int:news_id>/', methods=['GET'])
def get(news_id: int):
    """
    Retorna uma noticia especifica

    Args:
        news_id (int): Identificador da noticia
    """    
    try:
        news = News.query.filter_by(id=news_id)
        news = news.first()
        if news:
            response = NewsSchema().dumps(news), 200
        else:
            response = {'status': 'News {} doesn\'t exist'.format(news_id)}, 404
    except ValidationError as err:
        response = err.messages, 400

    return response

@bp_news.route('/', methods=['POST'])
def create():
    """
    Valida JSON da requisição e persiste nova noticia
    """    
    try:
        news = NewsSchema().load(request.json) 
        db.session.add(news)
        db.session.commit()

        response = NewsSchema().dump(news), 201
    except ValidationError as err:
        response = err.messages, 400
    except IntegrityError as err:
        response = {'status': f'{err.__cause__}'}, 400
    
    return response

@bp_news.route('/<int:news_id>/', methods=['PUT'])
def update(news_id: int):
    """
    Valida JSON da requisição e atualiza nova noticia

    Args:
        news_id (int): Identificador da noticia
    """    
    try:
        news = News.query.filter_by(id=news_id)
        if news.first():     
            request_json = json.loads(request.data)   
            news.update(request_json)
            db.session.commit()
            response = request_json, 200
        else:
            response = {'status': 'News {} doesn\'t exist'.format(news_id)}, 404
    except ValidationError as err:
        response = err.messages, 400
    except IntegrityError as err:
        response = {'status': f'{err.__cause__}'}, 400
    
    return response


@bp_news.route('/<int:news_id>/', methods=['DELETE'])
def delete(news_id: int):
    """
    Deleta noticia cadastrada

    Args:
        news_id (int): Identificador da noticia
    """    
    try:
        news = News.query.filter_by(id=news_id).first()

        if news:
            db.session.delete(news)
            db.session.commit()
            
            response = {'status': 'News {} deleted with success'.format(news_id)}, 200
        else:
            response = {'status': 'News {} doesn\'t exist'.format(news_id)}, 404
    except ValidationError as err:
        response = err.messages, 400
    
    return response
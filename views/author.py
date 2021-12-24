import json, os
from flask import Blueprint, request
from models.author import Author
from schemas.author import AuthorSchema
from services.database import db
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

bp_authors = Blueprint('authors', __name__, url_prefix='/authors')


@bp_authors.route('/', methods=['GET'])
def list():
    """
    Lista todos autores cadastrados
    """    
    try:
        authors = Author.query.all()
        response = AuthorSchema(many=True).dumps(authors), 200
    except ValidationError as err:
        response = err.messages, 400
    
    return response

@bp_authors.route('/<int:author_id>/', methods=['GET'])
def get(author_id: int):
    """
    Retorna um autor especifico

    Args:
        author_id (int): Identificador do autor
    """    
    try:
        authors = Author.query.filter_by(id=author_id)
        author = authors.first()
        if author:
            response = AuthorSchema().dumps(author), 200
        else:
            response = {'status': 'Author {} doesn\'t exist'.format(author_id)}, 404
    except ValidationError as err:
        response = err.messages, 400

    return response

@bp_authors.route('/', methods=['POST'])
def create():
    """
    Valida JSON da requisição e persiste novo autor
    """    
    try:
        author = AuthorSchema().load(request.json) 
        db.session.add(author)
        db.session.commit()

        response = AuthorSchema().dump(author), 201
    except ValidationError as err:
        response = err.messages, 400
    except IntegrityError as err:
        response = {'status': f'{err.__cause__}'}, 400
    
    return response

@bp_authors.route('/<int:author_id>/', methods=['PUT'])
def update(author_id: int):
    """
    Valida JSON da requisição e atualiza novo autor

    Args:
        author_id (int): Identificador do autor
    """    
    try:
        author = Author.query.filter_by(id=author_id)
        if author.first():     
            request_json = json.loads(request.data)   
            author.update(request_json)
            db.session.commit()
            response = request_json, 200
        else:
            response = {'status': 'Author {} doesn\'t exist'.format(author_id)}, 404
    except ValidationError as err:
        response = err.messages, 400
    except IntegrityError as err:
        response = {'status': f'{err.__cause__}'}, 400
    
    return response


@bp_authors.route('/<int:author_id>/', methods=['DELETE'])
def delete(author_id: int):
    """
    Delete autor cadastrado

    Args:
        author_id (int): Identificador do autor
    """    
    try:
        author = Author.query.filter_by(id=author_id).first()

        if author:
            db.session.delete(author)
            db.session.commit()
            
            response = {'status': 'Author {} deleted with success'.format(author_id)}, 200
        else:
            response = {'status': 'Author {} doesn\'t exist'.format(author_id)}, 404
    except ValidationError as err:
        response = err.messages, 400
    
    return response
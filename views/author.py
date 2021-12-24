import json, os
from flask import Blueprint, request
from models.author import Author
from schemas.author import AutomationSchema
from services.database import db
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

bp_authors = Blueprint('authors', __name__, url_prefix='/authors')


@bp_authors.route('/', methods=['GET'])
def list():
    return {"result": "list"}

@bp_authors.route('/<int:author_id>/', methods=['GET'])
def get(author_id: int):
    return {"result": "get one"}

@bp_authors.route('/', methods=['POST'])
def create():
    return {"result": "create"}

@bp_authors.route('/<int:author_id>/', methods=['PUT'])
def update(author_id: int):
    return {"result": "update"}


@bp_authors.route('/<int:author_id>/', methods=['DELETE'])
def delete(author_id: int):
    return {"result": "delete"}
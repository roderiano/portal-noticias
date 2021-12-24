from marshmallow_sqlalchemy import field_for, fields
from services.marshmallow import ma
from models.news import News
from schemas.author import AuthorSchema

class NewsSchema(ma.SQLAlchemyAutoSchema):
    id = field_for(News, 'id', dump_only=True)
    author_id = field_for(News, 'author_id', load_only=True)
    author = fields.Nested(AuthorSchema)

    class Meta:
        model = News
        load_instance = True
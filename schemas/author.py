from marshmallow_sqlalchemy import field_for
from services.marshmallow import ma
from models.author import Author

class AutomationSchema(ma.SQLAlchemyAutoSchema):
    id = field_for(Author, 'id', dump_only=True)

    class Meta:
        model = Author
        load_instance = True
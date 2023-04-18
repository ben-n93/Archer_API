from flask import make_response, abort, request
from config import db
from models import Character, character_schema, characters_schema

def read_all():
    name = request.args.get('name')
    if name:
        print(name)
        characters = Character.query.filter(Character.name.like(f'%{name}%')).all()
        return characters_schema.dump(characters)
    else:
        characters = Character.query.all()
        return characters_schema.dump(characters)

def read_one(id):
    character = Character.query.filter(Character.id == id).one_or_none()
    print("ping")
    if character is not None:
        return character_schema.dump(character)
    else:
        abort(404, f"Character with {id} not found.")

def read_multiple(ids):
    characters = Character.query.filter(Character.id.in_(ids)).all()
    if characters:
        return characters_schema.dump(characters)
    else:
        abort(404, f"Character IDs not found.")

    
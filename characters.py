from flask import abort, request
from models import Character, character_schema, characters_schema

def read_all():
    """
    Return all characters data or, if name parameter passed in URL,
    character data associated with characters with exact or similar name.
    """
    name = request.args.get('name')
    if name:
        characters = Character.query.filter(Character.name.like(f'%{name}%')).all()
        return characters_schema.dump(characters)
    if not name:
        characters = Character.query.all()
        return characters_schema.dump(characters)

def read_one(character_id):
    """
    Return character date for the specified character.
    """
    print("Ping")
    character = Character.query.filter(Character.id == character_id).one_or_none()
    if character is not None:
        return character_schema.dump(character)
    if character is None:
        abort(404, f"Character with {character_id} not found.")

def read_multiple(character_ids):
    """
    Return multiple character data for the specified characters.
    """
    characters = Character.query.filter(Character.id.in_(character_ids)).all()
    if characters:
        return characters_schema.dump(characters)
    if not characters:
        abort(404, "Character IDs not found.")

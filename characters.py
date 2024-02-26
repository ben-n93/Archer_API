from flask import abort, request
import models


def read_all():
    """
    Return all characters data or, if name parameter passed in URL,
    character data associated with characters with exact or similar name.
    """
    name = request.args.get("name")
    if name:
        characters = models.Character.query.filter(
            models.Character.name.like(f"%{name}%")
        ).all()
        return models.characters_schema.dump(characters)
    if not name:
        characters = models.Character.query.all()
        return models.characters_schema.dump(characters)


def read_one(character_id):
    """
    Return character date for the specified character.
    """
    print("Episode:", character_id)
    character = models.Character.query.filter(
        models.Character.id == character_id
    ).one_or_none()
    if character is not None:
        return models.character_schema.dump(character)
    if character is None:
        abort(404, f"Character with {character_id} not found.")

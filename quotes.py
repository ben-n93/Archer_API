import random

from flask import abort, request
from config import db
import models


def read_all():
    """
    Return all quotes data or, if character name parameter passed, return
    quotes data associated with characters with a similar name.
    """
    character = request.args.get("character")
    if character:
        quotes = models.Quote.query.filter(
            models.Quote.character.like(f"%{character}%")
        ).all()
        return models.quotes_schema.dump(quotes)
    else:
        quotes = models.Quote.query.all()
        return models.quotes_schema.dump(quotes)


def read_one(quote_id):
    """
    Return a quote with the specified id.
    """
    quote = models.Quote.query.filter(models.Quote.id == quote_id).one_or_none()
    if quote is not None:
        return models.quote_schema.dump(quote)
    else:
        abort(404, f"Quote with {quote_id} not found.")


def get_random():
    """
    Return a random quote.
    """
    count = db.session.query(db.func.count(models.Quote.id)).scalar()
    random_number = random.randint(1, count)
    quote = models.Quote.query.filter(models.Quote.id == random_number).one_or_none()
    if quote:
        return models.quote_schema.dump(quote)
    else:
        abort(404, "Error.")

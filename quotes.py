from flask import make_response, abort
from config import db
import models 

def read_all():
    quotes = models.Quote.query.all()
    return models.quotes_schema.dump(quotes)

def read_one(id):
    quote = models.Quote.query.filter(models.Quote.id == id).one_or_none()
    if quote is not None:
        return models.quote_schema.dump(quote)
    else:
        abort(404, f"Quote with {id} not found.")

def read_multiple(ids):
    quotes = models.Quote.query.filter(models.Quote.id.in_(ids)).all()
    if quotes:
        return models.quotes_schema.dump(quotes)
    else:
        abort(404, f"Quotes IDs not found.")
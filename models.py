from config import db, ma
from marshmallow_sqlalchemy import fields


class Quote(db.Model):
    __tablename__ = "quotes"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    quote = db.Column(db.String(32))
    character = db.Column(db.String, db.ForeignKey("characters.name"))
    episode = db.Column(db.String(32))


class QuoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Quote
        load_instance = True
        sqla_session = db.session
        include_fk = True


quote_schema = QuoteSchema()
quotes_schema = QuoteSchema(many=True)


class Character(db.Model):
    __tablename__ = "characters"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(32))
    aliases = db.Column(db.String(32))
    occupations = db.Column(db.String(32))
    voice_actor = db.Column(db.String(32))
    first_appearance = db.Column(db.String(32))
    include_relationships = True
    quotes = db.relationship(Quote, backref="quotes")


class CharacterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Character
        load_instance = True
        sqla_session = db.session
        include_fk = True
        include_relationships = True

    quotes = fields.Nested("QuoteSchema", many=True)


character_schema = CharacterSchema()
characters_schema = CharacterSchema(many=True)


class Episode(db.Model):
    __tablename__ = "episodes"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(32))
    season = db.Column(db.Integer)
    ep_number = db.Column(db.Integer)
    original_air_date = db.Column(db.String(32))
    writers = db.Column(db.String(32))
    director = db.Column(db.String(32))


class EpisodeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Episode
        load_instance = True
        sqla_session = db.session
        include_fk = True


episode_schema = EpisodeSchema()
episodes_schema = EpisodeSchema(many=True)

from flask import make_response, abort
from config import db
import models 

def read_all():
    episodes = models.Episode.query.all()
    return models.episodes_schema.dump(episodes)

def read_one(id):
    episode = models.Episode.query.filter(models.Episode.id == id).one_or_none()
    if episode is not None:
        return models.episode_schema.dump(episode)
    else:
        abort(404, f"Episode with {id} not found.")

def read_multiple(ids):
    episodes = models.Episode.query.filter(models.Episode.id.in_(ids)).all()
    if episodes:
        return models.episodes_schema.dump(episodes)
    else:
        abort(404, f"Episode IDs not found.")
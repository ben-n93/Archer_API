from flask import abort
import models


def read_all():
    """
    Return all episodes data.
    """
    episodes = models.Episode.query.all()
    return models.episodes_schema.dump(episodes)


def read_one(episode_id):
    """
    Return episode data for the specified episode.
    """
    episode = models.Episode.query.filter(models.Episode.id == episode_id).one_or_none()
    if episode is not None:
        return models.episode_schema.dump(episode)
    if episode is None:
        abort(404, f"Episode with {episode_id} not found.")

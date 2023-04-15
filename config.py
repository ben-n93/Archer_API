import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = pathlib.Path(__file__).parent.resolve()
connex_app = connexion.App(__name__, specification_dir=basedir)

app = connex_app.app
#app.config.update(JSON_SORT_KEYS=False)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'archer_data.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
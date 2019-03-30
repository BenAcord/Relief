from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlite3 import Connection as SQLite3Connection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'odd5tW5QEK-3H98ewJYQVMpX-Ueq1y4kk30kyqhHI8c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/relief.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

from relief import routes
from relief.models import Campaigns, ReliefConfig, CyberKillChains
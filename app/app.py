from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


# Create App Object #
app = Flask(__name__)
app.config.from_object(Configuration)

# Create DB Object #
db = SQLAlchemy(app)

# Migrations #
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)



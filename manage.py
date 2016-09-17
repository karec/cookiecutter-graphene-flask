from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from main_api.app import create_app
from main_api.extensions import db

app = create_app()

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(debug=True)


if __name__ == "__main__":
    manager.run()

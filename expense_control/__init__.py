from celery import Celery
from flask import Flask
from flask_migrate import Migrate

from expense_control.db import db
from expense_control.shared.storage import Storage
from expense_control.shared.singleton import Singleton


class App(metaclass=Singleton):
    app = None

    def start(self):
        self.app = self.__create_application(config={}, db=db)
        self.__inject_blueprints(self.app)

        return self.app

    def initialize_celery(self):
        if not self.app:
            self.app = self.__create_application(config={}, db=db)

        app = self.app

        celery = Celery(app.import_name)
        celery.config_from_object('expense_control.config.celery_config')
        celery.conf.update(app.config)

        TaskBase = celery.Task

        class ContextTask(TaskBase):
            abstract = True

            def __call__(self, *args, **kwargs):
                with app.app_context():
                    return TaskBase.__call__(self, *args, **kwargs)

        celery.Task = ContextTask

        return celery

    def __create_application(self, config={}, db=None):
        app = Flask(__name__)
        app.config.from_pyfile('config/config.py')

        Migrate(app, db)
        db.init_app(app)

        Storage().setup_instance(db)
        return app

    def __inject_blueprints(self, app):
        from expense_control.controller.expense import app as expense_app
        from expense_control.controller.user import app as user_app

        app.register_blueprint(expense_app)
        app.register_blueprint(user_app)


celery = App().initialize_celery()

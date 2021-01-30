from flask import Flask
from plugins import api, db
from app.Course.view import course_bp

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Dev')

    db.init_app(app=app)
    api.init_app(app=app)

    bps = [course_bp]

    for bp in bps:
        app.register_blueprint(bp)

    return app
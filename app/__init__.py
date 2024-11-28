from flask import Flask

def create_app():
    app = Flask(__name__)

    from .db import pg as pg_db
    pg_db.init_app(app)

    from .views import init_views
    init_views(app)

    return app

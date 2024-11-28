from flask import request, render_template

from app.db.queries import ALL_SURVEYS
from app.db.pg import get_db_connection

def init_views(app):


    @app.route('/hello')
    def hello():
        return 'Hello world'


    @app.route('/')
    def all_surveys():
        if request.method == 'GET':
            conn = get_db_connection()
            with conn.cursor() as cursor:
                cursor.execute(ALL_SURVEYS)
                surveys = cursor.fetchall()

        return render_template('all_surveys.html', all_surveys=surveys)

    return app
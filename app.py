# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение


from flask import Flask
from flask_restx import Api

from config import Config
from models import Movie, Genre, Director
from setup_db import db
from views.movies import movies_ns
from views.genre import genre_ns
from views.directors import director_ns


# функция создания основного объекта app
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.app.config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 4}
    api.add_namespace(movies_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    create_data(app, db)


# функция
def create_data(app, db):
    with app.app_context():
         db.create_all()
         f1 = Movie(title="Вооружен", description="События происходят", trailer="https://www.youtube.com/watch?v=hLA5631F-jo", year=1978, rating=6)
         sp1 = Genre(name="Комедия")
         sp2 = Director(name="Декстер Флетчер")
         with db.session.begin():
             db.session.add_all([f1])
             db.session.add_all([sp1, sp2])

#         создать несколько сущностей чтобы добавить их в БД
#
#         with db.session.begin():
#             db.session.add_all(здесь список созданных объектов)
#


app = create_app(Config())
app.debug = True
if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)




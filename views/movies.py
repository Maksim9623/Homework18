# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service
from flask import request
from flask_restx import Resource, Namespace
from models import db, Movie, MovieSchema


movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
     """ Вьюшка для получения get и post запросов"""
     def get(self):
          director_id = request.args.get('director_id')
          genre_id = request.args.get('genre_id')
          year = request.args.get('year')
          if director_id:
               movies = Movie.query.filter(Movie.director_id == director_id)
          elif genre_id:
               movies = Movie.query.filter(Movie.genre_id == genre_id)
          elif year:
               movies = Movie.query.filter(Movie.year == year)
          else:
               movies = Movie.query.all()
          return MovieSchema(many=True).dump(movies), 200

     def post(self):
          req_json = request.json
          new_movie = Movie(**req_json)

          with db.session.begin():
               db.session.add(new_movie)

          return "", 201


@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    """ Вьюшка для получения get, put, delete запросов"""
    def get(self, mid):
        one_movies = Movie.query.get(mid)
        return MovieSchema().dump(one_movies), 200

    def put(self, mid):
        data = request.json
        movie = Movie.query.get(mid)
        movie.title = data['title']
        movie.description = data['description']
        movie.trailer = data['trailer']
        movie.year = data['year']
        movie.rating = data['rating']
        movie.genre_id = data['genre_id']
        movie.director_id = data['director_id']

        db.session.add(movie)
        db.session.commit()
        db.session.close()
        return "Успешное обновление", 201

    def delete(self, mid: int):
        movie = Movie.query.get(mid)
        if not movie:
            return "", 404

        db.session.delete(movie)
        db.session.commit()

        return "", 204

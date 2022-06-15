from flask_restx import Resource, Namespace
from models import Genre, GenreSchema

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    """ Вьюшка для получения get запроса для жанров """
    def get(self):
        genre = Genre.query.all()
        return GenreSchema(many=True).dump(genre), 200


@genre_ns.route('/<int:bid>')
class GenreView(Resource):
    """ Вьюшка для получения get запроса для одного жанра"""
    def get(self, bid):
        one_genre = Genre.query.get(bid)
        return GenreSchema().dump(one_genre), 200

from flask_restx import Resource, Namespace
from models import Director, DirectorSchema

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    """ Вьюшка для получения get запроса для режиссеров """
    def get(self):
        director = Director.query.all()
        return DirectorSchema(many=True).dump(director), 200


@director_ns.route('/<int:bid>')
class DirectorView(Resource):
    """ Вьюшка для получения get запроса для одного режиссера"""
    def get(self, bid):
        one_director = Director.query.get(bid)
        return DirectorSchema().dump(one_director), 200

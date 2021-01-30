from flask import Blueprint, jsonify
from flask_restful import Resource

from plugins import api

course_bp = Blueprint('course', __name__)

class CoursesAPI(Resource):
    def get(self):
        return jsonify(
            message='cources api',
            status=200
      )

api.add_resource(CoursesAPI, '/courses')
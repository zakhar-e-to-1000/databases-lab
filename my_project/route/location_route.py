from flask import Blueprint

from my_project.controller.location_controller import *

bp = Blueprint("location_bp", __name__, url_prefix='/api/location')

bp.add_url_rule('/', view_func=get_locations_list, methods=['GET'])
bp.add_url_rule('/<int:id>', view_func=get_location, methods=['GET'])

bp.add_url_rule('/', view_func=post_location, methods=['POST'])

bp.add_url_rule('/<int:id>', view_func=put_location, methods=['PUT'])
bp.add_url_rule('/<int:id>', view_func=delete_location, methods=['DELETE'])

bp.add_url_rule('/<int:id>/measurement-points',
                view_func=get_measurement_points, methods=["GET"])
bp.add_url_rule('/<int:id>/rivers',
                view_func=get_rivers, methods=["GET"])

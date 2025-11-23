from flask import Blueprint

from my_project.controller.measurement_point_controller import *

bp = Blueprint("measurement_point_bp", __name__,
               url_prefix='/api/measurement-point')

bp.add_url_rule('/', view_func=get_measurement_point_list, methods=['GET'])
bp.add_url_rule('/<int:id>', view_func=get_measurement_point, methods=['GET'])

bp.add_url_rule('/', view_func=post_measurement_point, methods=['POST'])

bp.add_url_rule('/<int:id>', view_func=put_measurement_point, methods=['PUT'])
bp.add_url_rule('/<int:id>', view_func=delete_measurement_point,
                methods=['DELETE'])

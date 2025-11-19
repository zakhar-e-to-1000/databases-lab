from flask import Blueprint

from my_project.controller.river_controller import *

bp = Blueprint('river_bp', __name__, url_prefix='/api/river')

bp.add_url_rule('/', view_func=get_rivers_list, methods=['GET'])
bp.add_url_rule('/<int:id>', view_func=get_river, methods=['GET'])

bp.add_url_rule('/', view_func=post_river, methods=['POST'])

bp.add_url_rule('/<int:id>', view_func=put_river, methods=['PUT'])
bp.add_url_rule('/<int:id>', view_func=delete_river, methods=['DELETE'])

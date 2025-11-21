from flask import Blueprint

from my_project.controller.region_controller import *

bp = Blueprint("region_bp", __name__, url_prefix='/api/region')

bp.add_url_rule('/', view_func=get_regions_list, methods=['GET'])
bp.add_url_rule('/<int:id>', view_func=get_region, methods=['GET'])

bp.add_url_rule('/', view_func=post_region, methods=['POST'])

bp.add_url_rule('/<int:id>', view_func=put_region, methods=['PUT'])
bp.add_url_rule('/<int:id>', view_func=delete_region, methods=['DELETE'])

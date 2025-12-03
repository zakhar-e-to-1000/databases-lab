from flask import Blueprint
from my_project.controller.procedures_controller import *

bp = Blueprint("procedures_db", __name__, url_prefix="/api/proc")

bp.add_url_rule('/1', view_func=quick_insert_location, methods=['POST'])
bp.add_url_rule('/2', view_func=random_10, methods=['POST'])
bp.add_url_rule('/3', view_func=convinient_insert, methods=['POST'])
bp.add_url_rule('/4/<string:func>', view_func=get_stat, methods=['GET'])

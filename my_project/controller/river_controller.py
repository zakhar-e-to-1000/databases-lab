from my_project.service.river_service import RiverService
from flask import jsonify, request


from pydantic import BaseModel, ConfigDict, ValidationError


class River(BaseModel):
    model_config = ConfigDict(extra='forbid')
    name: str
    length: float


svc = RiverService()


def get_rivers_list():
    result = svc.get_all()

    data = [dict(row)['River'].to_dict() for row in result]
    return jsonify(data)


def post_river():
    try:
        data = River.model_validate(request.json)
    except ValidationError:
        return "Invalid JSON", 400
    name = data.name
    length = data.length
    res = svc.post(name, length)
    if res is None:
        return "Unique keys (or other database integrity) error", 400
    else:
        return res.to_dict(), 201


def get_river(id):
    r = svc.get(id)
    if r == None:
        return "Not found", 404
    return jsonify(r.to_dict()), 200


def put_river(id):
    try:
        data = River.model_validate(request.json)
    except ValidationError:
        return "Invalid JSON", 400
    name = data.name
    length = data.length
    does_exists, new_r = svc.update(id, name, length)
    if not does_exists:
        return "Not Found", 404
    if new_r is None:
        return "Unique columns (or other database integriry) error", 400
    return jsonify(new_r.to_dict()), 200


def delete_river(id):
    if svc.delete(id):
        return "Success", 200
    else:
        return "Not found", 404

from my_project.service.river_service import RiverService
from flask import jsonify, request

svc = RiverService()


def get_rivers_list():
    result = svc.get_all()

    data = [dict(row)['River'].to_dict() for row in result]
    return jsonify(data)


def post_river():
    data = request.json or {}
    name = data['name']
    length = data['length']
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
    data = request.json or {}
    new_name = data['name']
    new_length = data['length']
    does_exists, new_r = svc.update(id, new_name, new_length)
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

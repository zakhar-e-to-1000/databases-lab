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
    return svc.post(name, length).to_dict(), 202


def get_river(id):
    r = svc.get(id)
    if r == None:
        return "Not found", 404
    return jsonify(r.to_dict()), 202


def put_river(id):
    data = request.json or {}
    new_name = data['name']
    new_length = data['length']
    new_r = svc.update(id, new_name, new_length)
    if new_r is None:
        return "Not Found", 404
    else:
        return jsonify(new_r.to_dict()), 200


def delete_river(id):
    if svc.delete(id):
        return "Success", 200
    else:
        return "Not found", 404

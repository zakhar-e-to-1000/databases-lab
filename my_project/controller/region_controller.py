from my_project.service.region_service import RegionService
from flask import jsonify, request

svc = RegionService()


def get_rivers_list():
    result = svc.get_all()

    data = [dict(row)['Region'].to_dict() for row in result]
    return jsonify(data)


def post_river():
    data = request.json or {}
    name = data['name']
    return svc.post(name).to_dict(), 202


def get_river(id):
    r = svc.get(id)
    if r == None:
        return "Not found", 404
    return jsonify(r.to_dict()), 202


def put_river(id):
    data = request.json or {}
    new_name = data['name']
    new_r = svc.update(id, new_name)
    if new_r is None:
        return "Not Found", 404
    else:
        return jsonify(new_r.to_dict()), 200


def delete_river(id):
    if svc.delete(id):
        return "Success", 200
    else:
        return "Not found", 404

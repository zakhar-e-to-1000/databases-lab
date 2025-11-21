from my_project.service.measurement_point_service import MeasumentPointService
from flask import jsonify, request

svc = MeasumentPointService()


def get_rivers_list():
    result = svc.get_all()

    data = [dict(row)['Region'].to_dict() for row in result]
    return jsonify(data)


def post_river():
    data = request.json or {}
    river_id = data['river_id']
    location_id = data['location_id']
    description = data['description']

    return svc.post(river_id, location_id, description).to_dict(), 202


def get_river(id):
    r = svc.get(id)
    if r == None:
        return "Not found", 404
    return jsonify(r.to_dict()), 202


def put_river(id):
    data = request.json or {}
    river_id = data['river_id']
    location_id = data['location_id']
    description = data['description']
    new_r = svc.update(id, river_id, location_id, description)
    if new_r is None:
        return "Not Found", 404
    else:
        return jsonify(new_r.to_dict()), 200


def delete_river(id):
    if svc.delete(id):
        return "Success", 200
    else:
        return "Not found", 404

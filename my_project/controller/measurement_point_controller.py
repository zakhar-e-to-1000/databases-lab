from my_project.service.measurement_point_service import MeasumentPointService
from flask import jsonify, request

svc = MeasumentPointService()


def get_measurement_point_list():
    result = svc.get_all()

    data = [dict(row)['Region'].to_dict() for row in result]
    return jsonify(data)


def post_measurement_point():
    data = request.json or {}
    river_id = data['river_id']
    location_id = data['location_id']
    description = data['description']

    res = svc.post(river_id, location_id, description)
    if res is None:
        return "Unique keys (or other database integrity) error", 400
    else:
        return res.to_dict(), 201


def get_measurement_point(id):
    r = svc.get(id)
    if r == None:
        return "Not found", 404
    return jsonify(r.to_dict()), 200


def put_measurement_point(id):
    data = request.json or {}
    river_id = data['river_id']
    location_id = data['location_id']
    description = data['description']
    does_exists, new_r = svc.update(id, river_id, location_id, description)
    if not does_exists:
        return "Not Found", 404
    if new_r is None:
        return "Unique columns (or other database integriry) error", 400
    return jsonify(new_r.to_dict()), 200


def delete_measurement_point(id):
    if svc.delete(id):
        return "Success", 200
    else:
        return "Not found", 404

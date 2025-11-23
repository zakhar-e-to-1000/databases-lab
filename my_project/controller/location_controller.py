from my_project.service.location_service import LocationService
from flask import jsonify, request

svc = LocationService()


def get_locations_list():
    result = svc.get_all()

    data = [dict(row)['Location'].to_dict() for row in result]
    return jsonify(data)


def post_location():
    data = request.json or {}
    name = data['name']
    region_id = data['region_id']
    latitude = data['latitude']
    longitude = data['longitude']
    res = svc.post(name, region_id, latitude, longitude)
    if res is None:
        return "Unique keys (or other database integrity) error"
    else:
        return res.to_dict(), 201


def get_location(id):
    r = svc.get(id)
    if r == None:
        return "Not found", 404
    return jsonify(r.to_dict()), 200


def put_location(id):
    data = request.json or {}
    name = data['name']
    region_id = data['region_id']
    latitude = data['latitude']
    longitude = data['longitude']

    does_exists, new_r = svc.update(id, name, region_id, latitude, longitude)
    if not does_exists:
        return "Not Found", 404
    if new_r is None:
        return "Unique columns (or other database integriry) error", 400
    return jsonify(new_r.to_dict()), 200


def delete_location(id):
    if svc.delete(id):
        return "Success", 200
    else:
        return "Not found", 404

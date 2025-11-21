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
    return svc.post(name, region_id, latitude, longitude).to_dict(), 202


def get_location(id):
    r = svc.get(id)
    if r == None:
        return "Not found", 404
    return jsonify(r.to_dict()), 202


def put_location(id):
    data = request.json or {}
    name = data['name']
    region_id = data['region_id']
    latitude = data['latitude']
    longitude = data['longitude']

    new_r = svc.update(id, name, region_id, latitude, longitude)
    if new_r is None:
        return "Not Found", 404
    else:
        return jsonify(new_r.to_dict()), 200


def delete_location(id):
    if svc.delete(id):
        return "Success", 200
    else:
        return "Not found", 404

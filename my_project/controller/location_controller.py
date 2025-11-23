from my_project.service.location_service import LocationService
from flask import jsonify, request
from pydantic import BaseModel, ConfigDict, ValidationError


class Location(BaseModel):
    model_config = ConfigDict(extra='forbid')
    name: str
    region_id: int
    latitude: float
    longitude: float


svc = LocationService()


def get_locations_list():
    result = svc.get_all()

    data = [dict(row)['Location'].to_dict() for row in result]
    return jsonify(data)


def post_location():
    try:
        data = Location.model_validate(request.json)
    except ValidationError:
        return "Invalid JSON", 400
    name = data.name
    region_id = data.region_id
    latitude = data.latitude
    longitude = data.longitude
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
    try:
        data = Location.model_validate(request.json)
    except ValidationError:
        return "Invalid JSON", 400
    name = data.name
    region_id = data.region_id
    latitude = data.latitude
    longitude = data.longitude

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


def get_measurement_points(id):
    points = svc.get_measurement_points(id)
    if points is None:
        return "Location not found", 404
    res = [i.to_dict() for i in points]
    return res, 200

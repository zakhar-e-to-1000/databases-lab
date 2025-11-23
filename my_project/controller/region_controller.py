from my_project.service.region_service import RegionService
from flask import jsonify, request

from pydantic import BaseModel, ConfigDict, ValidationError


class Region(BaseModel):
    model_config = ConfigDict(extra='forbid')
    name: str


svc = RegionService()


def get_regions_list():
    result = svc.get_all()

    data = [dict(row)['Region'].to_dict() for row in result]
    return jsonify(data)


def post_region():
    try:
        data = Region.model_validate(request.json)
    except ValidationError:
        return "Invalid JSON", 400
    name = data.name
    res = svc.post(name)
    if res is None:
        return "Unique keys (or other database integrity) error", 400
    else:
        return res.to_dict(), 201


def get_region(id):
    r = svc.get(id)
    if r == None:
        return "Not found", 404
    return jsonify(r.to_dict()), 200


def put_region(id):
    try:
        data = Region.model_validate(request.json)
    except ValidationError:
        return "Invalid JSON", 400
    name = data.name
    does_exists, new_r = svc.update(id, name)
    if not does_exists:
        return "Not Found", 404
    if new_r is None:
        return "Unique columns (or other database integriry) error", 400
    return jsonify(new_r.to_dict()), 200


def delete_region(id):
    if svc.delete(id):
        return "Success", 200
    else:
        return "Not found", 404


def get_locations(id):
    locations = svc.get_locations(id)
    if locations is None:
        return "Region not Found", 404
    res = [i.to_dict() for i in locations]
    return res, 200

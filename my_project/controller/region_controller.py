from my_project.service.region_service import RegionService
from flask import jsonify, request

svc = RegionService()


def get_regions_list():
    result = svc.get_all()

    data = [dict(row)['Region'].to_dict() for row in result]
    return jsonify(data)


def post_region():
    data = request.json or {}
    name = data['name']
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
    data = request.json or {}
    new_name = data['name']
    does_exists, new_r = svc.update(id, new_name)
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

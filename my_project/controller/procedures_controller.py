from pydantic import BaseModel, ConfigDict, ValidationError
from my_project.dao.procedures_dao import ProcDao
from flask import request
dao = ProcDao()


class quickBase(BaseModel):
    model_config = ConfigDict(extra='forbid')
    location_name: str
    region_name: str


class convBase(BaseModel):
    model_config = ConfigDict(extra='forbid')
    river_name: str
    location_name: str


def quick_insert_location():
    try:
        data = quickBase.model_validate(request.json)
    except ValidationError:
        return "Invalid JSON", 400
    location_name = data.location_name
    region_name = data.region_name
    return str(dao.quick_insert_location(location_name, region_name)[0]), 200
    # return 'ok', 200


def random_10():
    dao.random_10()
    return 'ok', 200


def convinient_insert():
    try:
        data = convBase.model_validate(request.json)
    except ValidationError:
        return "Invalid JSON", 400
    river_name = data.river_name
    location_name = data.location_name
    return str(dao.convinient_insert(river_name, location_name)[0]), 200
    # return 'ok', 200


def get_stat(func: str):
    return {"number": dao.get_stat(func)[0][0]}, 200

from my_project.dao.location_dao import LocationDao


class LocationService:
    def __init__(self) -> None:
        self.dao = LocationDao()

    def get(self, id):
        return self.dao.get(id)

    def post(self, name, region_id, latitude, longitude):
        return self.dao.create(name, region_id, latitude, longitude)

    def get_all(self):
        return self.dao.get_all()

    def delete(self, id):
        return self.dao.delete(id)

    def update(self, id, new_name, new_region_id, new_latitude, new_longitude):
        return self.dao.update(id, new_name, new_region_id, new_latitude, new_longitude)

    def get_measurement_points(self, id):
        return self.dao.get_measurement_points(id)

    def get_rivers(self, id):
        return self.dao.get_rivers(id)

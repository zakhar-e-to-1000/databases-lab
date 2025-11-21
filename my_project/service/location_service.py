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
        r = self.dao.get(id)
        if r is None:
            return False
        self.dao.delete(r)
        return True

    def update(self, id, new_name, new_region_id, new_latitude, new_longitude):
        r = self.dao.get(id)
        if r is None:
            return None
        return self.dao.update(r, new_name, new_region_id, new_latitude, new_longitude)

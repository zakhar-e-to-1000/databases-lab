from my_project.dao.measurement_point_dao import MeasumentPointDao


class MeasumentPointService:
    def __init__(self) -> None:
        self.dao = MeasumentPointDao()

    def get(self, id):
        return self.dao.get(id)

    def post(self, river_id, location_id, description):
        return self.dao.create(river_id, location_id, description)

    def get_all(self):
        return self.dao.get_all()

    def delete(self, id):
        r = self.dao.get(id)
        if r is None:
            return False
        self.dao.delete(r)
        return True

    def update(self, id, river_id, location_id, description):
        r = self.dao.get(id)
        if r is None:
            return None
        return self.dao.update(r, river_id, location_id, description)

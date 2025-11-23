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
        return self.dao.delete(id)

    def update(self, id, river_id, location_id, description):
        return self.dao.update(id, river_id, location_id, description)

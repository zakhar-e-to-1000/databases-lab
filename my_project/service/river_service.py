from my_project.dao.river_dao import RiverDao


class RiverService:
    def __init__(self) -> None:
        self.dao = RiverDao()

    def get(self, id):
        return self.dao.get(id)

    def post(self, name, length):
        return self.dao.create(name, length)

    def get_all(self):
        return self.dao.get_all()

    def delete(self, id):
        return self.dao.delete(id)

    def update(self, id, new_name, new_length):
        return self.dao.update(id, new_name, new_length)

    def get_measurement_points(self, id):
        return self.dao.get_measurement_points(id)

    def get_locations(self, id):
        return self.dao.get_locations(id)

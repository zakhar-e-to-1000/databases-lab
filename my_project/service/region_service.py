from my_project.dao.region_dao import RegionDao


class RegionService:
    def __init__(self) -> None:
        self.dao = RegionDao()

    def get(self, id):
        return self.dao.get(id)

    def post(self, name):
        return self.dao.create(name)

    def get_all(self):
        return self.dao.get_all()

    def delete(self, id):
        return self.dao.delete(id)

    def update(self, id, new_name):
        return self.dao.update(id, new_name)

    def get_locations(self, id):
        return self.dao.get_locations(id)

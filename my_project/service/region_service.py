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
        r = self.dao.get(id)
        if r is None:
            return False
        self.dao.delete(r)
        return True

    def update(self, id, new_name):
        r = self.dao.get(id)
        if r is None:
            return None
        return self.dao.update(r, new_name)

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
        r = self.dao.get(id)
        if r is None:
            return False
        self.dao.delete(r)
        return True

    def update(self, id, new_name, new_length):
        r = self.dao.get(id)
        if r is None:
            return None
        return self.dao.update(r, new_name, new_length)

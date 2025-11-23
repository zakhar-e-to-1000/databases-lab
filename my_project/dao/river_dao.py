from extensions import db
from my_project.domain.river import River
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError


class RiverDao:
    def create(self, name, length):
        r = River(name=name, length=length)  # type: ignore
        db.session.add(r)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return None
        return r

    def get(self, id):
        r = db.session.get(River, id)
        return r

    def get_all(self):
        list = db.session.execute(
            select(River)
        ).mappings().all()
        return list

    def delete(self, id):
        r = self.get(id)
        if r is None:
            return False
        db.session.delete(r)
        db.session.commit()
        return True

    def update(self, id, new_name, new_length):
        r = self.get(id)
        if r is None:
            return (False, None)

        r.name = new_name
        r.length = new_length

        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return (True, None)
        return (True, r)

    def get_measurement_points(self, id):
        r = self.get(id)
        if r is None:
            return None
        return r.measurement_points

    def get_locations(self, id):
        r = self.get(id)
        if r is None:
            return None
        return r.locations

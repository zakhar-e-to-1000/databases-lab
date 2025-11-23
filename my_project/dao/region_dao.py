from extensions import db
from my_project.domain.region import Region
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError


class RegionDao:
    def create(self, name):
        r = Region(name=name)  # type: ignore
        db.session.add(r)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return None
        return r

    def get(self, id):
        r = db.session.get(Region, id)
        return r

    def get_all(self):
        list = db.session.execute(
            select(Region)
        ).mappings().all()
        return list

    def delete(self, id):
        r = self.get(id)
        if r is None:
            return False
        db.session.delete(r)
        db.session.commit()
        return True

    def update(self, id, new_name):
        r = self.get(id)
        if r is None:
            return (False, None)

        r.name = new_name

        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return (True, None)
        return (True, r)

    def get_locations(self, id):
        r = self.get(id)
        if r is None:
            return None
        return r.locations

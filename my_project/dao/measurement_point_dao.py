from extensions import db
from my_project.domain.measurement_point import MeasumentPoint
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError


class MeasumentPointDao:
    def create(self, river_id, location_id, description):
        r = MeasumentPoint(river_id=river_id, location_id=location_id,  # type: ignore
                           description=description)  # type: ignore
        db.session.add(r)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return None
        return r

    def get(self, id):
        r = db.session.get(MeasumentPoint, id)
        return r

    def get_all(self):
        list = db.session.execute(
            select(MeasumentPoint)
        ).mappings().all()
        return list

    def delete(self, id):
        r = self.get(id)
        if r is None:
            return False
        db.session.delete(r)
        db.session.commit()
        return True

    def update(self, id: MeasumentPoint, river_id, location_id, description):
        r = self.get(id)
        if r is None:
            return (False, None)
        r.river_id = river_id,
        r.location_id = location_id,
        r.description = description
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return (True, None)
        return (True, r)

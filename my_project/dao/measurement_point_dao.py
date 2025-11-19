from extensions import db
from my_project.domain.measurement_point import MeasumentPoint
from sqlalchemy import select


class MeasumentPointDaO:
    def create(self, river_id, location_id, description):
        r = MeasumentPoint(name=name, river_id=river_id, location_id=location_id,  # type: ignore
                           description=description)  # type: ignore
        db.session.add(r)
        db.session.commit()
        return r

    def get(self, id):
        r = db.session.get(MeasumentPoint, id)
        return r

    def get_all(self):
        list = db.session.execute(
            select(MeasumentPoint)
        ).mappings().all()
        return list

    def delete(self, r: MeasumentPoint):
        db.session.delete(r)
        db.session.commit()

    def update(self, r: MeasumentPoint, river_id, location_id, description):
        r.river_id = river_id,
        r.location_id = location_id,
        r.description = description
        db.session.commit()
        return r

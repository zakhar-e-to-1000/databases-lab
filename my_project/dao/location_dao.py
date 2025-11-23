from extensions import db
from my_project.domain.location import Location
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError


class LocationDao:
    def create(self, name, region_id, latitude, longitude):
        r = Location(name=name, region_id=region_id,  # type: ignore
                     latitude=latitude, longitude=longitude)  # type: ignore
        db.session.add(r)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return None
        return r

    def get(self, id):
        r = db.session.get(Location, id)
        return r

    def get_all(self):
        list = db.session.execute(
            select(Location)
        ).mappings().all()
        return list

    def delete(self, id):
        r = self.get(id)
        if r is None:
            return False
        db.session.delete(r)
        db.session.commit()
        return True

    def update(self, id, new_name, new_region_id, new_latitude, new_longitude):
        r = self.get(id)
        if r is None:
            return (False, None)
        r.name = new_name
        r.region_id = new_region_id
        r.latitude = new_latitude
        r.longitude = new_longitude
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

    def get_rivers(self, id):
        r = self.get(id)
        if r is None:
            return None
        return r.rivers

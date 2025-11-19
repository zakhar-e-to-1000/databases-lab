from extensions import db
from my_project.domain.location import Location
from sqlalchemy import select


class LocationDao:
    def create(self, name, region_id, latitude, longitude):
        r = Location(name=name, region_id=region_id,  # type: ignore
                     latitude=latitude, longitude=longitude)  # type: ignore
        db.session.add(r)
        db.session.commit()
        return r

    def get(self, id):
        r = db.session.get(Location, id)
        return r

    def get_all(self):
        list = db.session.execute(
            select(Location)
        ).mappings().all()
        return list

    def delete(self, r: Location):
        db.session.delete(r)
        db.session.commit()

    def update(self, r, new_name, new_region_id, new_latitude, new_longitude):
        r.name = new_name
        db.session.commit()
        return r

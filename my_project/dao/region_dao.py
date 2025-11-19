from extensions import db
from my_project.domain.region import Region
from sqlalchemy import select


class RegionDao:
    def create(self, name):
        r = Region(name=name)  # type: ignore
        db.session.add(r)
        db.session.commit()
        return r

    def get(self, id):
        r = db.session.get(Region, id)
        return r

    def get_all(self):
        list = db.session.execute(
            select(Region)
        ).mappings().all()
        return list

    def delete(self, r: Region):
        db.session.delete(r)
        db.session.commit()

    def update(self, r, new_name):
        r.name = new_name
        db.session.commit()
        return r

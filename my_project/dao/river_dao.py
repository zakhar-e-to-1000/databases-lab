from extensions import db
from my_project.domain.river import River
from sqlalchemy import select


class RiverDao:
    def create(self, name, length):
        r = River(name=name, length=length)
        db.session.add(r)
        db.session.commit()
        return r

    def get(self, id):
        r = db.session.get(River, id)
        return r

    def get_all(self):
        list = db.session.execute(
            db.select(River)
        ).mappings().all()
        return list

    def delete(self, r: River):
        db.session.delete(r)
        db.session.commit()

    def update(self, r, new_name, new_length):
        r.name = new_name
        r.length = new_length
        db.session.commit()
        return r

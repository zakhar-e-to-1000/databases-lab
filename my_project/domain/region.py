from extensions import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, mapped_column

from my_project.domain.measurement_point import MeasumentPoint


class Region(db.Model):
    __tablename__ = 'region'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(100), unique=True, nullable=False)
    locations = relationship(
        'Location', back_populates='region')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

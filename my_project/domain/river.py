from sqlalchemy import Integer, String, Double
from sqlalchemy.orm import relationship, mapped_column
from extensions import db
from my_project.domain.measurement_point import MeasumentPoint


class River(db.Model):
    __tablename__ = 'river'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(100), unique=True, nullable=False)
    length = mapped_column(Double)
    measurement_points = relationship(
        'MeasumentPoint', back_populates='river')
    locations = relationship(
        'Location', secondary='measurement_point')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'length': self.length
        }

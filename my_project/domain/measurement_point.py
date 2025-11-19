from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Integer, Text
from sqlalchemy.orm import mapped_column
from extensions import db


class MeasumentPoint(db.Model):
    __tablename__ = 'measurement_point'
    id = mapped_column(Integer, primary_key=True)
    river_id = mapped_column(ForeignKey('river.id'), nullable=False)
    location_id = mapped_column(ForeignKey('location.id'), nullable=False)
    description = mapped_column(Text, nullable=True)

    river = relationship('River', back_populates='measurement_points')
    location = relationship('Location', back_populates='measurement_points')

    def to_dict(self):
        return {
            'id': self.id,
            'river_id': self.river_id,
            'location_id': self.location_id,
            'description': self.description
        }

from sqlalchemy import Integer, String, Double, ForeignKey
from sqlalchemy.orm import relationship, mapped_column
from extensions import db
from my_project.domain.measurement_point import MeasumentPoint


class Location(db.Model):
    __tablename__ = 'location'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(100), unique=True, nullable=False)
    region_id = mapped_column(ForeignKey('region.id'), nullable=False)
    latitude = mapped_column(Double)
    longitude = mapped_column(Double)

    region = relationship('Region', back_populates='locations')
    measurement_points = relationship(
        'MeasumentPoint', back_populates='location')

    rivers = relationship(
        "River", secondary="measurement_point")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'region_id': self.region_id,
            'latitude': self.latitude,
            'longitude': self.longitude,
        }

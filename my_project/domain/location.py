from sqlalchemy.orm import relationship
from extensions import db
import sqlalchemy as sa


class Location(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), unique=True, nullable=False)
    region_id = db.Column(db.Integer, sa.ForeignKey(
        "region.id", ondelete='CASCADE'), nullable=False,)
    region = relationship("region", back_populates='locations')
    measurement_points = relationship(
        'measurement_point', back_populates='location')

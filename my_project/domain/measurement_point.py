from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column
from extensions import db
from sqlalchemy import Integer


class Measument_Point(db.Model):
    __tablename__ = 'measurement_point'
    id = mapped_column(Integer, primary_key=True)
    river_id = mapped_column(ForeignKey('river.id'), nullable=False)
    location_id = mapped_column(ForeignKey('location'), nullable=False)

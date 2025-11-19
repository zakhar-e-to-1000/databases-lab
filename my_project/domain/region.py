from sqlalchemy.orm import relationship
from extensions import db


class Region(db.Model):
    __tablename__ = "region"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), unique=True, nullable=False)
    locations = relationship("location", back_populates="region")

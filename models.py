from sqlalchemy import Column, Integer, String
from database import Base


class Item(Base):
    __tablename__ = "items"

    # id is primary key (unique identifier for each item)
    # name and description will store text data
    id = Column(Integer, primary_key=True, index=True)
    # index=True makes searching faster for this column
    name = Column(String, index=True, unique=True)
    description = Column(String, index=True)

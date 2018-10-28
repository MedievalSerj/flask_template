from .table import city_table
from ..basic import Base


class City(Base):
    __table__ = city_table

    def __repr__(self):
        return self.name

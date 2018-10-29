from ..basic import Base
from .table import city_table


class City(Base):
    __table__ = city_table

    def __repr__(self):
        return self.name

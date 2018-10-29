import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

from ..basic import metadata

city_table = sa.Table(
    'city',
    metadata,
    sa.Column('id', UUID, primary_key=True,
              server_default=sa.text('uuid_generate_v1()')),
    sa.Column('name', sa.String(64), unique=True)
)

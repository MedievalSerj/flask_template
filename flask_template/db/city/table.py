import sqlalchemy as sa
from ..basic import metadata
from sqlalchemy.dialects.postgresql import UUID


city_table = sa.Table(
    'city',
    metadata,
    sa.Column('id', UUID, primary_key=True,
              server_default=sa.text('uuid_generate_v1()')),
    sa.Column('name', sa.String(64))
)

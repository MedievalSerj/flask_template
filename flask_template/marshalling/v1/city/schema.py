from marshmallow import Schema, fields


class CitySchema(Schema):
    id = fields.UUID(dump_only=True)
    name = fields.String(required=True)

from marshmallow import (
    Schema, fields, validate, ValidationError, validates_schema
)


class BlogPostUpSertSchema(Schema):
    id = fields.Integer(required=False)
    title = fields.String(required=True, validate=validate.Length(min=1, max=100))
    content = fields.String(required=True, validate=validate.Length(min=1, max=10000))

    @validates_schema
    def validate_title(self, data, **kwargs):
        if not data.get("title") or len(data.get("title").strip()) == 0:
            raise ValidationError({"title": "this field can not be blank"})

    @validates_schema
    def validate_content(self, data, **kwargs):
        if not data.get("content") or len(data.get("content").strip()) == 0:
            raise ValidationError({"content": "this field can not be blank"})

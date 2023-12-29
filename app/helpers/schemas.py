from marshmallow import Schema, validate, validates, validates_schema,  ValidationError, fields as ma_fields, post_load
from datetime import date, datetime
from app.helpers.dataclasses import DatastoreData


class CustomDateField(ma_fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        try:
            return datetime.strptime(value, "%d/%m/%Y").date()
        except ValueError:
            raise ValidationError("Data inválida.")


class CustomDateTimeField(ma_fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        try:
            return datetime.strptime(value, "%Y-%m-%d %H:%M:%S.%f")
        except ValueError:
            raise ValidationError("Data inválida.")


class DateInputSchema(Schema):

    initial_date = ma_fields.Date(required=True)
    finish_date = ma_fields.Date(required=True)
    quantity = ma_fields.Integer(required=True, min=0, max=100)
    document = ma_fields.String(allow_none=True)
    begin_sequence = ma_fields.Integer(allow_none=True, min=0)
    end_sequence = ma_fields.Integer(allow_none=True, min=0)

    @validates("finish_date")
    def validate_initial(self, value):
        print("VALUE", value, type(value))
        if value > date.today():
            raise ValidationError("Data final não pode ser futura")
        return True

    @validates_schema
    def validate_dates(self, data, **kwargs):
        if data.get("finish_date") < data.get("initial_date"):
            raise ValidationError("Data final tem que ser maior ou igual a data inicial")


class RecordsSchema(Schema):
    class Meta:
        unknown = 'exclude'  # Irá excluir campos desconhecidos

    @post_load
    def make_instance(self, data, **kwargs):
        return DatastoreData(**data)

    cnm = ma_fields.String()
    date_request = CustomDateTimeField()
    document = ma_fields.String()
    ip = ma_fields.String()
    name = ma_fields.String()
    number = ma_fields.Integer()
    url = ma_fields.String(allow_none=True)
    motivo = ma_fields.String(allow_none=True)
    value = ma_fields.Float()
    ip_cliente = ma_fields.String(allow_none=True)

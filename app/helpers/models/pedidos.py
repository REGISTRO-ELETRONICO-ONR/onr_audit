from google.cloud import ndb


class Pedidos(ndb.Model):

    name = ndb.StringProperty(required=True)
    document = ndb.StringProperty(required=True)
    number = ndb.IntegerProperty(required=True)
    cnm = ndb.StringProperty(required=True)
    date_request = ndb.DateTimeProperty(required=True)
    value = ndb.FloatProperty(required=True)
    ip = ndb.StringProperty(required=True)
    url = ndb.TextProperty()
    pedido_id = ndb.IntegerProperty(required=True)
    motivo = ndb.StringProperty()
    ip_cliente = ndb.StringProperty()

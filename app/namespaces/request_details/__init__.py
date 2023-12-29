from flask_restx import Namespace
from .views import registro_rotas

#namespace usado

RD_ns = Namespace('Request Details',
                  description='Endpoints relacionadas a informações sobre os pedidos de visualização de matrícula')

# registro as rotas utilizando injeção de dependencia
registro_rotas(RD_ns)

from flask_restx import Namespace
from .views import registro_rotas


#namespace usado


Credential_ns = Namespace('Credential',
                  description='Endpoints relacionadas a auditar projetos',)

# registro as rotas utilizando injeção de dependencia
registro_rotas(Credential_ns)

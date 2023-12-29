from flask_restx import Resource
from flask import request
from .swagger import CredentialSwagger
from .services.credential import Credential
from app.helpers.exceptions import CredentialNotSent
from app.helpers.services.gcp_auth import GCPAuth
from .services.pattern_finder import PatternFinder
from .services.gcp_info import GCPInfo
from .services.cnm import CNM
from .dataclasses import FinderData


def registro_rotas(namespace):
    credential_post = CredentialSwagger()

    @namespace.route("/register")
    class GerarPedido(Resource):
        @namespace.expect(credential_post.expect(namespace))
        @namespace.marshal_with(credential_post.marshal_with(namespace))
        @namespace.doc(**credential_post.doc)
        def post(self):
            payload = request.json
            if not payload:
                return {"message": "credencial não enviada"}, 400

            try:
                credential = Credential()
                credential.register(payload)
            except (TypeError, PermissionError, OSError):
                return {"message": "erro no sistema ao criar credencial"}, 500
            except CredentialNotSent:
                return {"message": "credencial não enviada"}, 500

            try:
                datastore_client = GCPAuth.datastore_auth(payload.get("credential"))
                storage_client = GCPAuth.storage_auth(payload.get("credential"))
            except Exception as e:
                print(e)
                return {"message": "credenciais inválidas"}, 400

            try:
                gcp_info = GCPInfo(storage_client)
                pattern_finder = PatternFinder(gcp_info)

                project_id = payload.get("credential").get("project_id")
                cns = project_id.split("-")[-1].zfill(6)
                matriculas = [1500, 1000, 500, 10]

                for matricula in matriculas:
                    cnm = CNM().create(cns, matricula)
                    finder_data = FinderData(project_id, matricula, cnm)
                    if pattern_finder.find_image(finder_data):
                        break

                    return {"message": "padrão não identificad"}, 400

            except Exception as e:
                print(e)
                return {"message": "padrão não identificado"}, 400

            return {"message": "credencial registrada no sistema"}

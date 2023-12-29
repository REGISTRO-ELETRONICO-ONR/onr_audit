import datetime

from flask_restx import Resource
from flask import request, abort
from .swagger import RequestDetailsSwagger
from app.helpers.schemas import DateInputSchema, RecordsSchema
from app.helpers.repositories.records_db import RecordsDb
from app.helpers.services.convert_datetime import ConvertDatetime
from marshmallow import ValidationError as ma_ValidationError
from app.helpers.services.gcp_auth import GCPAuth
from app.helpers.services.get_credential import GetCredential
from .services.rankings import Ranking


def registro_rotas(namespace):

    request_detail_swagger = RequestDetailsSwagger()

    @namespace.route("/ranking-usuarios-pago")
    class RankingUsuariosPagos(Resource):
        @namespace.doc(**request_detail_swagger.doc)
        @namespace.marshal_with(request_detail_swagger.marshal_with_usuarios(namespace))
        def get(self):
            try:
                credential = GetCredential.get()
                gcp_auth = GCPAuth()
                ndb_client = gcp_auth.datastore_auth(credential)

                data_in = request.args
                data_out = DateInputSchema().load({"initial_date": data_in.get("initial_date"),
                                                   "finish_date": data_in.get("finish_date"),
                                                   "quantity": data_in.get("quantity")})

                with ndb_client.context(namespace="vm-engine"):
                    records = RecordsDb().get(data_out.get("initial_date"), data_out.get("finish_date"))

                records_dict_list = [record.to_dict() for record in records]
                records_with_correct_date_request = ConvertDatetime().convert_to_str(records_dict_list)

                records_objects = RecordsSchema(many=True).load(records_with_correct_date_request)
                result = Ranking(records_objects, data_out.get("quantity")).ranking_documento(paid=True)

                return {"result": result}

            except ma_ValidationError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e.messages}")
            except ValueError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e}")
            except Exception as e:
                print(f"erro: {e}")
                abort(500, f"Erro ao processar pedido")

    @namespace.route("/ranking-usuarios-gratis")
    class RankingUsuariosGratis(Resource):
        @namespace.doc(**request_detail_swagger.doc)
        @namespace.marshal_with(request_detail_swagger.marshal_with_usuarios(namespace))
        def get(self):
            try:
                credential = GetCredential.get()
                gcp_auth = GCPAuth()
                ndb_client = gcp_auth.datastore_auth(credential)

                data_in = request.args
                data_out = DateInputSchema().load({"initial_date": data_in.get("initial_date"),
                                                   "finish_date": data_in.get("finish_date"),
                                                   "quantity": data_in.get("quantity")})

                with ndb_client.context(namespace="vm-engine"):
                    records = RecordsDb().get(data_out.get("initial_date"), data_out.get("finish_date"))

                records_dict_list = [record.to_dict() for record in records]
                records_with_correct_date_request = ConvertDatetime().convert_to_str(records_dict_list)

                records_objects = RecordsSchema(many=True).load(records_with_correct_date_request)
                result = Ranking(records_objects, data_out.get("quantity")).ranking_documento(paid=False)

                return {"result": result}

            except ma_ValidationError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e.messages}")
            except ValueError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e}")
            except Exception as e:
                print(f"erro: {e}")
                abort(500, f"Erro ao processar pedido")

    @namespace.route("/ranking-usuarios-fds-pago")
    class RankingUsuariosFdsPaid(Resource):
        @namespace.doc(**request_detail_swagger.doc)
        @namespace.marshal_with(request_detail_swagger.marshal_with_usuarios(namespace))
        def get(self):
            try:
                credential = GetCredential.get()
                gcp_auth = GCPAuth()
                ndb_client = gcp_auth.datastore_auth(credential)

                data_in = request.args
                data_out = DateInputSchema().load({"initial_date": data_in.get("initial_date"),
                                                   "finish_date": data_in.get("finish_date"),
                                                   "quantity": data_in.get("quantity")})

                with ndb_client.context(namespace="vm-engine"):
                    records = RecordsDb().get(data_out.get("initial_date"), data_out.get("finish_date"))

                records_dict_list = [record.to_dict() for record in records]
                records_with_correct_date_request = ConvertDatetime().convert_to_str(records_dict_list)

                records_objects = RecordsSchema(many=True).load(records_with_correct_date_request)
                result = Ranking(records_objects, data_out.get("quantity")).ranking_documento_fds(paid=True)

                return {"result": result}

            except ma_ValidationError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e.messages}")
            except ValueError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e}")
            except Exception as e:
                print(f"erro: {e}")
                abort(500, f"Erro ao processar pedido")

    @namespace.route("/ranking-usuarios-fds-gratis")
    class RankingUsuariosFdsGratis(Resource):
        @namespace.doc(**request_detail_swagger.doc)
        @namespace.marshal_with(request_detail_swagger.marshal_with_usuarios(namespace))
        def get(self):
            try:
                credential = GetCredential.get()
                gcp_auth = GCPAuth()
                ndb_client = gcp_auth.datastore_auth(credential)

                data_in = request.args
                data_out = DateInputSchema().load({"initial_date": data_in.get("initial_date"),
                                                   "finish_date": data_in.get("finish_date"),
                                                   "quantity": data_in.get("quantity")})

                with ndb_client.context(namespace="vm-engine"):
                    records = RecordsDb().get(data_out.get("initial_date"), data_out.get("finish_date"))

                records_dict_list = [record.to_dict() for record in records]
                records_with_correct_date_request = ConvertDatetime().convert_to_str(records_dict_list)

                records_objects = RecordsSchema(many=True).load(records_with_correct_date_request)
                result = Ranking(records_objects, data_out.get("quantity")).ranking_documento_fds(paid=False)

                return {"result": result}

            except ma_ValidationError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e.messages}")
            except ValueError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e}")
            except Exception as e:
                print(f"erro: {e}")
                abort(500, f"Erro ao processar pedido")

    @namespace.route("/ranking-usuarios-motivo")
    class RankingUsuariosMotivo(Resource):
        @namespace.doc(**request_detail_swagger.doc_motivo)
        @namespace.marshal_with(request_detail_swagger.marshal_with_motive(namespace))
        def get(self):
            try:
                credential = GetCredential.get()
                gcp_auth = GCPAuth()
                ndb_client = gcp_auth.datastore_auth(credential)

                data_in = request.args
                if not data_in.get("document"):
                    abort(400, "document is mandatory")

                document = data_in.get("document").replace("-", "").replace("/", "").replace(".", "")
                data_out = DateInputSchema().load({"initial_date": data_in.get("initial_date"),
                                                   "finish_date": data_in.get("finish_date"),
                                                   "quantity": data_in.get("quantity"),
                                                   "document": document})

                with ndb_client.context(namespace="vm-engine"):
                    records = RecordsDb().get(data_out.get("initial_date"),
                                              data_out.get("finish_date"),
                                              data_out.get("document"))

                records_dict_list = [record.to_dict() for record in records]
                records_with_correct_date_request = ConvertDatetime().convert_to_str(records_dict_list)

                records_objects = RecordsSchema(many=True).load(records_with_correct_date_request)
                result = Ranking(records_objects, data_out.get("quantity")).ranking_documento_motive()

                return {"result": result}

            except ma_ValidationError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e.messages}")
            except ValueError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e}")
            except Exception as e:
                print(f"erro: {e}")
                abort(500, f"Erro ao processar pedido")

    @namespace.route("/ranking-ip-onr-apps")
    class RankingIp(Resource):
        @namespace.doc(**request_detail_swagger.doc)
        @namespace.marshal_with(request_detail_swagger.marshal_with_ip_address(namespace))
        def get(self):
            try:
                credential = GetCredential.get()
                gcp_auth = GCPAuth()
                ndb_client = gcp_auth.datastore_auth(credential)

                data_in = request.args
                data_out = DateInputSchema().load({"initial_date": data_in.get("initial_date"),
                                                   "finish_date": data_in.get("finish_date"),
                                                   "quantity": data_in.get("quantity")})

                with ndb_client.context(namespace="vm-engine"):
                    records = RecordsDb().get(data_out.get("initial_date"), data_out.get("finish_date"))

                records_dict_list = [record.to_dict() for record in records]
                records_with_correct_date_request = ConvertDatetime().convert_to_str(records_dict_list)

                records_objects = RecordsSchema(many=True).load(records_with_correct_date_request)
                result = Ranking(records_objects, data_out.get("quantity")).ranking_ip_onr_apps()

                return {"result": result}

            except ma_ValidationError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e.messages}")
            except ValueError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e}")
            except Exception as e:
                print(f"erro: {e}")
                abort(500, f"Erro ao processar pedido")

    @namespace.route("/ranking-ip-cliente-pago")
    class RankingIpClientePaid(Resource):
        @namespace.doc(**request_detail_swagger.doc)
        @namespace.marshal_with(request_detail_swagger.marshal_with_ip_address(namespace))
        def get(self):
            try:
                credential = GetCredential.get()
                gcp_auth = GCPAuth()
                ndb_client = gcp_auth.datastore_auth(credential)

                data_in = request.args
                data_out = DateInputSchema().load({"initial_date": data_in.get("initial_date"),
                                                   "finish_date": data_in.get("finish_date"),
                                                   "quantity": data_in.get("quantity")})

                with ndb_client.context(namespace="vm-engine"):
                    records = RecordsDb().get(data_out.get("initial_date"), data_out.get("finish_date"))

                records_dict_list = [record.to_dict() for record in records]
                for record in records_dict_list:
                    print(record)
                records_with_correct_date_request = ConvertDatetime().convert_to_str(records_dict_list)

                records_objects = RecordsSchema(many=True).load(records_with_correct_date_request)
                result = Ranking(records_objects, data_out.get("quantity")).ranking_client_ip(paid=True)

                return {"result": result}

            except ma_ValidationError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e.messages}")
            except ValueError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e}")
            except Exception as e:
                print(f"erro: {e}")
                abort(500, f"Erro ao processar pedido")

    @namespace.route("/ranking-ip-cliente-gratis")
    class RankingIpClienteFree(Resource):
        @namespace.doc(**request_detail_swagger.doc)
        @namespace.marshal_with(request_detail_swagger.marshal_with_ip_address(namespace))
        def get(self):
            try:
                credential = GetCredential.get()
                gcp_auth = GCPAuth()
                ndb_client = gcp_auth.datastore_auth(credential)

                data_in = request.args
                data_out = DateInputSchema().load({"initial_date": data_in.get("initial_date"),
                                                   "finish_date": data_in.get("finish_date"),
                                                   "quantity": data_in.get("quantity")})

                with ndb_client.context(namespace="vm-engine"):
                    records = RecordsDb().get(data_out.get("initial_date"), data_out.get("finish_date"))

                records_dict_list = [record.to_dict() for record in records]
                for record in records_dict_list:
                    print(record)
                records_with_correct_date_request = ConvertDatetime().convert_to_str(records_dict_list)

                records_objects = RecordsSchema(many=True).load(records_with_correct_date_request)
                result = Ranking(records_objects, data_out.get("quantity")).ranking_client_ip(paid=False)

                return {"result": result}

            except ma_ValidationError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e.messages}")
            except ValueError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e}")
            except Exception as e:
                print(f"erro: {e}")
                abort(500, f"Erro ao processar pedido")

    @namespace.route("/ranking-solicitacoes-mesmo-minuto-pago")
    class RankingSolicitacoesMesmoMinutoPago(Resource):
        @namespace.doc(**request_detail_swagger.doc)
        @namespace.marshal_with(request_detail_swagger.marshal_with_same_minute(namespace))
        def get(self):
            try:
                credential = GetCredential.get()
                gcp_auth = GCPAuth()
                ndb_client = gcp_auth.datastore_auth(credential)

                data_in = request.args
                data_out = DateInputSchema().load({"initial_date": data_in.get("initial_date"),
                                                   "finish_date": data_in.get("finish_date"),
                                                   "quantity": data_in.get("quantity")})

                with ndb_client.context(namespace="vm-engine"):
                    records = RecordsDb().get(data_out.get("initial_date"), data_out.get("finish_date"))

                records_dict_list = [record.to_dict() for record in records]
                records_with_correct_date_request = ConvertDatetime().convert_to_str(records_dict_list)

                records_objects = RecordsSchema(many=True).load(records_with_correct_date_request)
                result = Ranking(records_objects, data_out.get("quantity")).ranking_documento_same_minuto(paid=True)

                return {"result": result}

            except ma_ValidationError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e.messages}")
            except ValueError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e}")
            except Exception as e:
                print(f"erro: {e}")
                abort(500, f"Erro ao processar pedido")

    @namespace.route("/ranking-solicitacoes-mesmo-minuto-gratis")
    class RankingSolicitacoesMesmoMinutoGratis(Resource):
        @namespace.doc(**request_detail_swagger.doc)
        @namespace.marshal_with(request_detail_swagger.marshal_with_same_minute(namespace))
        def get(self):
            try:
                credential = GetCredential.get()
                gcp_auth = GCPAuth()
                ndb_client = gcp_auth.datastore_auth(credential)

                data_in = request.args
                data_out = DateInputSchema().load({"initial_date": data_in.get("initial_date"),
                                                   "finish_date": data_in.get("finish_date"),
                                                   "quantity": data_in.get("quantity")})

                with ndb_client.context(namespace="vm-engine"):
                    records = RecordsDb().get(data_out.get("initial_date"), data_out.get("finish_date"))

                records_dict_list = [record.to_dict() for record in records]
                records_with_correct_date_request = ConvertDatetime().convert_to_str(records_dict_list)

                records_objects = RecordsSchema(many=True).load(records_with_correct_date_request)
                result = Ranking(records_objects, data_out.get("quantity")).ranking_documento_same_minuto(paid=False)

                return {"result": result}

            except ma_ValidationError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e.messages}")
            except ValueError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e}")
            except Exception as e:
                print(f"erro: {e}")
                abort(500, f"Erro ao processar pedido")

    @namespace.route("/ranking-sequencia-gratis")
    class RankingSequenceFree(Resource):
        @namespace.doc(**request_detail_swagger.doc)
        @namespace.marshal_with(request_detail_swagger.marshal_sequence(namespace))
        def get(self):
            try:
                credential = GetCredential.get()
                gcp_auth = GCPAuth()
                ndb_client = gcp_auth.datastore_auth(credential)

                data_in = request.args
                data_out = DateInputSchema().load({"initial_date": data_in.get("initial_date"),
                                                   "finish_date": data_in.get("finish_date"),
                                                   "quantity": data_in.get("quantity")})

                with ndb_client.context(namespace="vm-engine"):
                    records = RecordsDb().get(data_out.get("initial_date"), data_out.get("finish_date"))

                records_dict_list = [record.to_dict() for record in records]
                records_with_correct_date_request = ConvertDatetime().convert_to_str(records_dict_list)

                records_objects = RecordsSchema(many=True).load(records_with_correct_date_request)
                result = Ranking(records_objects, data_out.get("quantity")).ranking_sequence(paid=False)

                return {"result": result}

            except ma_ValidationError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e.messages}")
            except ValueError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e}")
            except Exception as e:
                print(f"erro: {e}")
                abort(500, f"Erro ao processar pedido")

    @namespace.route("/ranking-sequencia-pago")
    class RankingSequencePaid(Resource):
        @namespace.doc(**request_detail_swagger.doc)
        @namespace.marshal_with(request_detail_swagger.marshal_sequence(namespace))
        def get(self):
            try:
                credential = GetCredential.get()
                gcp_auth = GCPAuth()
                ndb_client = gcp_auth.datastore_auth(credential)

                data_in = request.args
                data_out = DateInputSchema().load({"initial_date": data_in.get("initial_date"),
                                                   "finish_date": data_in.get("finish_date"),
                                                   "quantity": data_in.get("quantity")})

                with ndb_client.context(namespace="vm-engine"):
                    records = RecordsDb().get(data_out.get("initial_date"), data_out.get("finish_date"))

                records_dict_list = [record.to_dict() for record in records]
                records_with_correct_date_request = ConvertDatetime().convert_to_str(records_dict_list)

                records_objects = RecordsSchema(many=True).load(records_with_correct_date_request)
                result = Ranking(records_objects, data_out.get("quantity")).ranking_sequence(paid=True)

                return {"result": result}

            except ma_ValidationError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e.messages}")
            except ValueError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e}")
            except Exception as e:
                print(f"erro: {e}")
                abort(500, f"Erro ao processar pedido")

    @namespace.route("/ranking-sequencia-details-gratis")
    class RankingSequenceDetailsFree(Resource):
        @namespace.doc(**request_detail_swagger.doc_sequence_details)
        @namespace.marshal_with(request_detail_swagger.marshal_sequence_details(namespace))
        def get(self):
            try:
                credential = GetCredential.get()
                gcp_auth = GCPAuth()
                ndb_client = gcp_auth.datastore_auth(credential)

                data_in = request.args
                data_out = DateInputSchema().load({"initial_date": data_in.get("initial_date"),
                                                   "finish_date": data_in.get("finish_date"),
                                                   "quantity": 100,  # coloquei um valor padrao so pra ter algo
                                                   "begin_sequence": data_in.get("begin_sequence"),
                                                   "end_sequence": data_in.get("end_sequence"),})

                with ndb_client.context(namespace="vm-engine"):
                    records = RecordsDb().get(data_out.get("initial_date"), data_out.get("finish_date"))

                records_dict_list = [record.to_dict() for record in records]
                records_with_correct_date_request = ConvertDatetime().convert_to_str(records_dict_list)

                records_objects = RecordsSchema(many=True).load(records_with_correct_date_request)

                begin = data_out.get("begin_sequence")
                end = data_out.get("end_sequence")
                result = Ranking(records_objects, data_out.get("quantity")).sequence_details(begin, end, paid=False)

                return {"result": result}

            except ma_ValidationError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e.messages}")
            except ValueError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e}")
            except Exception as e:
                print(f"erro: {e}")
                abort(500, f"Erro ao processar pedido")

    @namespace.route("/ranking-sequencia-details-pago")
    class RankingSequenceDetailsPaid(Resource):
        @namespace.doc(**request_detail_swagger.doc_sequence_details)
        @namespace.marshal_with(request_detail_swagger.marshal_sequence_details(namespace))
        def get(self):
            try:
                credential = GetCredential.get()
                gcp_auth = GCPAuth()
                ndb_client = gcp_auth.datastore_auth(credential)

                data_in = request.args
                data_out = DateInputSchema().load({"initial_date": data_in.get("initial_date"),
                                                   "finish_date": data_in.get("finish_date"),
                                                   "quantity": 100,  # coloquei um valor padrao so pra ter algo
                                                   "begin_sequence": data_in.get("begin_sequence"),
                                                   "end_sequence": data_in.get("end_sequence"), })

                with ndb_client.context(namespace="vm-engine"):
                    records = RecordsDb().get(data_out.get("initial_date"), data_out.get("finish_date"))

                records_dict_list = [record.to_dict() for record in records]
                records_with_correct_date_request = ConvertDatetime().convert_to_str(records_dict_list)

                records_objects = RecordsSchema(many=True).load(records_with_correct_date_request)

                begin = data_out.get("begin_sequence")
                end = data_out.get("end_sequence")
                result = Ranking(records_objects, data_out.get("quantity")).sequence_details(begin, end, paid=True)

                return {"result": result}

            except ma_ValidationError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e.messages}")
            except ValueError as e:
                print(f"erro: {e}")
                abort(400, f"Tipo de dado inválido: {e}")
            except Exception as e:
                print(f"erro: {e}")
                abort(500, f"Erro ao processar pedido")
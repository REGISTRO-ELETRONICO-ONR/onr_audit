from flask_restx import fields


class RequestDetailsSwagger:
    doc = {
        "params": {'initial_date': {'description': 'data de inicio do filtro', 'required': True,
                                    "example": "YYYY-mm-dd"},
                   'finish_date': {'description': 'data de fim do filtro', 'required': True,
                                        "example": "YYYY-mm-dd"},
                   'quantity': {'description': 'quantidade maxima desejada de dados na resposta', 'required': True,
                                "example": 100},
                   },
        "responses": {200: 'OK', 400: 'Bad Request', 404: 'Not Found', 500: 'Internal Error', 401: "Unauthorized"},
        "description": "Rota pra gerar o ranking do nome da rota",
        "security": 'apikey'}

    doc_motivo = {
        "params": {'initial_date': {'description': 'data de inicio do filtro', 'required': True,
                                    "example": "YYYY-mm-dd"},
                   'finish_date': {'description': 'data de fim do filtro', 'required': True,
                                   "example": "YYYY-mm-dd"},
                   'document': {'description': 'documento da entidade em específico', 'required': True,
                                "example": "XXX.XXX.XXX-XX"},
                   'quantity': {'description': 'quantidade maxima desejada de dados na resposta', 'required': True,
                                "example": 100}
                   },
        "responses": {200: 'OK', 400: 'Bad Request', 404: 'Not Found', 500: 'Internal Error', 401: "Unauthorized"},
        "description": "Rota pra gerar o ranking do nome da rota",
        "security": 'apikey'}

    doc_sequence_details = {
        "params": {'initial_date': {'description': 'data de inicio do filtro', 'required': True,
                                    "example": "YYYY-mm-dd"},
                   'finish_date': {'description': 'data de fim do filtro', 'required': True,
                                   "example": "YYYY-mm-dd"},
                   'begin_sequence': {'description': 'Numero da matricula onde a sequencia se inicia', 'required': True,
                                      "example": 10},
                   'end_sequence': {'description': 'Numero da matricula onde a sequencia finaliza', 'required': True,
                                    "example": 20}
                   },
        "responses": {200: 'OK', 400: 'Bad Request', 404: 'Not Found', 500: 'Internal Error', 401: "Unauthorized"},
        "description": "Rota pra gerar o ranking do nome da rota",
        "security": 'apikey'}

    @staticmethod
    def marshal_with_usuarios(namespace):
        document_output = namespace.model('RequestDetailsDocument',
                                          {"position": fields.Integer(description='Posição no ranking',
                                                                      example=1, ),
                                              "document": fields.String(description="documento do usuario. cpf/cnpj",
                                                                        example="xxx-xxx-xxx-xx", ),
                                              "name": fields.String(description="nome do usuario",
                                                                    example="Fulano da Silva", ),
                                              "quantity": fields.Integer(description="Quantidade de solicitações",
                                                                         example=1, )
                                           })

        request_detailt_result = namespace.model('RequestDetailDocumentResult', {"result": fields.Nested(document_output)})

        return request_detailt_result

    @staticmethod
    def marshal_with_ip_address(namespace):
        document_output = namespace.model('RequestDetailsDocumentIP',
                                          {"position": fields.Integer(description='Posição no ranking',
                                                                      example=1, ),
                                              "ip": fields.String(description="IP do usuario. ",
                                                                          example="0.0.0.0", ),
                                              "quantity": fields.Integer(description="Quantidade de solicitações",
                                                                         example=1, )
                                           })

        request_detailt_result = namespace.model('RequestDetailIPResult', {"result": fields.Nested(document_output)})

        return request_detailt_result

    @staticmethod
    def marshal_with_same_minute(namespace):
        document_output = namespace.model('RequestDetailsSameMinute',
                                          {"position": fields.Integer(description='Posição no ranking',
                                                                      example=1, ),
                                           "document": fields.String(description="documento do usuario. cpf/cnpj",
                                                                     example="xxx-xxx-xxx-xx", ),
                                           "name": fields.String(description="nome do usuario",
                                                                 example="Fulano da Silva", ),
                                           "quantity": fields.Integer(description="Quantidade de solicitações",
                                                                      example=1, ),
                                           "start_time": fields.String(description="Datetime da primeira solicitação",
                                                                       example="2023-11-09 16:41:34", )
                                           })

        request_detailt_result = namespace.model('RequestDetailSameMinuteResult',
                                                 {"result": fields.Nested(document_output)})

        return request_detailt_result

    @staticmethod
    def marshal_with_motive(namespace):
        document_output = namespace.model('RequestDetailsMotive',
                                          {"position": fields.Integer(description='Posição no ranking',
                                                                      example=1, ),
                                           "motive": fields.String(description="Motivo da solicitação",
                                                                     example="Tal notivo", ),
                                           "quantity": fields.Integer(description="Quantidade de solicitações",
                                                                      example=1, )
                                           })

        request_detailt_result = namespace.model('RequestDetailMotiveResult',
                                                 {"result": fields.Nested(document_output)})

        return request_detailt_result

    @staticmethod
    def marshal_sequence_details(namespace):
        document_output = namespace.model('RequestSequenceDetails',
                                          {"document": fields.String(description='CPF/CNPJ',
                                                                      example="00000000000"),
                                           "name": fields.String(description="nome da pessoa/empresa",
                                                                 example="Fulano da Silva"),
                                           "number": fields.Integer(description='Número da Matricula',
                                                                    example=1000),
                                           "ip_client": fields.String(description="IP do cliente que baixou",
                                                                      example="XXX.XXX.XXX.XXX"),
                                           "motive": fields.String(description="Motivo da solicitação",
                                                                   example="Tal motivo"),
                                           "value": fields.Float(description="Valor pago na visualização de matricula",
                                                                 example=2.5),
                                           "date_request": fields.String(description="Datetime da solicitação",
                                                                         example="2023-11-09 16:41:34", )
                                           })

        request_detailt_result = namespace.model('RequestSequenceDetailsResult',
                                                 {"result": fields.Nested(document_output)})

        return request_detailt_result

    @staticmethod
    def marshal_sequence(namespace):
        document_output = namespace.model('RequestDetailsSequence',
                                          {"position": fields.Integer(description='Posição no ranking',
                                                                      example=1, ),
                                           "begin_sequence": fields.Integer(description='Número do inicio da sequência',
                                                                            example=1000),
                                           "end_sequence": fields.Integer(description='Número do fim da sequência',
                                                                          example=1040),
                                           "size_sequence": fields.Integer(description='Tamanho da sequência',
                                                                           example=40),
                                           })

        request_detailt_result = namespace.model('RequestDetailSequenceResult',
                                                 {"result": fields.Nested(document_output)})

        return request_detailt_result

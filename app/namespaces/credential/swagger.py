from flask_restx import fields


class CredentialSwagger:

    doc = {
        "responses": {200: 'OK', 400: 'Bad Request', 404: 'Not Found', 500: 'Internal Error'},
        "description": "Registrar credencial no backend"}

    def __init__(self):
        self.example_credential = {
                  "type": "service_account",
                  "project_id": "projeto-onr",
                  "private_key_id": "xxxxxxxxxx",
                  "private_key": "-----BEGIN PRIVATE KEY----xxxxxxxxxxxxxxx-----END PRIVATE KEY-----\n",
                  "client_email": "app@projeto.com",
                  "client_id": "111111111111111",
                  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                  "token_uri": "https://oauth2.googleapis.com/token",
                  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/",
                  "universe_domain": "googleapis.com"
    }

    def expect(self, namespace):
        gerar_token_input = namespace.model('RegisterCredentialInput',
                                            {"credential": fields.Raw(description='json da credenial',
                                                                      example=self.example_credential)})

        return gerar_token_input

    @staticmethod
    def marshal_with(namespace):
        gerar_token_output = namespace.model('RegisterCredentialOutput',
                                             {"message": fields.String(description='mensagem de ok',
                                                                     example='registered', )})

        return gerar_token_output

import json


class GetCredential:

    @staticmethod
    def get():
        """
        método para pegar as credenciais no json, depois do registro da credencial ter sido realizado no endpoint
        indicado
        :return:
        """

        with open("auth.json", 'r') as file:
            credential = json.load(file)

        return credential

from app.helpers.exceptions import CredentialNotSent
import json


class Credential:

    @staticmethod
    def register(payload):
        """
        Método para registrar a credencial. Recebo os dados da credencial e gero um arquivo auth.json na raíz do projeto
        :param payload: credencial
        :return:
        """
        credential = payload.get("credential")
        if not credential:
            raise CredentialNotSent

        try:
            with open("auth.json", 'w') as f:
                json.dump(credential, f)
        except TypeError:
            raise TypeError
        except PermissionError:
            raise PermissionError
        except OSError:
            raise OSError

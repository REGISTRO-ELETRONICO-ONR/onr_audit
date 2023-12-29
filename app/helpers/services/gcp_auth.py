from google.cloud import ndb
from google.cloud import storage
from google.oauth2.service_account import Credentials


class GCPAuth:

    @staticmethod
    def datastore_auth(credential: dict) -> ndb.Client:
        """
        Helper para gerar autenticação com o datastore no GCP usando biblioteca ndb
        :param credential:
        :return:
        """
        project = credential.get("project_id")
        try:
            creds = Credentials.from_service_account_info(credential)
        except Exception as e:
            print(e)
            raise

        return ndb.Client(credentials=creds, project=project)

    @staticmethod
    def storage_auth(credential) -> storage.Client:
        """
        Helper para gerar autenticação com o datastore no GCP usando biblioteca ndb
        :param credential:
        :return:
        """

        project = credential.get("project_id")
        try:
            creds = Credentials.from_service_account_info(credential)
        except Exception as e:
            print(e)
            raise

        return storage.Client(credentials=creds, project=project)

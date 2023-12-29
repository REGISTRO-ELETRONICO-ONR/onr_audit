from google.auth.exceptions import DefaultCredentialsError, RefreshError
from google.cloud.exceptions import NotFound


class GCPInfo:
    """
    classe feita basicamente de métodos estaticos, apenas para evitar uso isolado de funções
    """

    def __init__(self, storage_client):
        self.storage_client = storage_client

    def get_bucket(self, project_id) -> object:
        """
        função para pegar o objeto bucket do GCP (onde se encontra todas as imagens do cartório)
        :param credential:
        :return:
        """

        try:
            # cns do DF tem um padrão diferente pra nome de bucket
            if "98707" in project_id:  # tratando a única exceção que foge a regra
                bucket_name = "bucket-rs-serafina-98707"
            elif "df" in project_id.split("-")[1]:
                partes = project_id.split("-")
                partes[0] = "bucket"
                bucket_name = "-".join(str(parte) for parte in partes)
            else:
                bucket_name = project_id.replace('projeto-onr', 'bucket')
            bucket = self.storage_client.bucket(bucket_name)
            return bucket
        except (ValueError, KeyError, DefaultCredentialsError, RefreshError, NotFound) as e:
            print(e)
            raise

    @staticmethod
    def get_blobs_and_image(bucket_name, directory, mat):
        try:
            prefix = 'IMG' + '/' + directory + '/' + mat
            blobs = bucket_name.list_blobs(prefix=prefix, delimiter=None)
            get_image = prefix

            return blobs, get_image

        except (ValueError, KeyError, DefaultCredentialsError, RefreshError, NotFound) as e:
            print(f"ERRO: {e}")
            # retorno falso em caso de alguma exceção ao pegar o blob
            raise

    @staticmethod
    def get_blob_multipage(bucket, directory, mat):
        """
        Função para fazer download da imagem multitiff no bucket. Importante mencionar que sempre é baixada a última
        versão da imagem que foi feita upload.
        :param bucket:
        :param directory:
        :param mat:
        :return:
        """

        try:
            blobs = [bucket.blob(blob_name='IMG' + '/' + directory + '/' + f'{mat}.tif'),
                     bucket.blob(blob_name='IMG' + '/' + directory + '/' + f'{mat}.TIF'),
                     bucket.blob(blob_name='IMG' + '/' + directory + '/' + f'{mat}.tiff'),
                     bucket.blob(blob_name='IMG' + '/' + directory + '/' + f'{mat}.TIFF')]

            blob_retornado = None
            for blob in blobs:
                if blob.exists():
                    blob.reload()  # Recarrega as propriedades do blob. Sem chamar essa função o GCP não me manda as infos.
                    if blob_retornado is None or blob.time_created > blob_retornado.time_created:
                        blob_retornado = blob

            return blob_retornado

        except (ValueError, KeyError, DefaultCredentialsError, RefreshError, NotFound) as e:
            print(f"O seguinte erro ocorreu: {e}")
            # retorno falso em caso de alguma exceção ao pegar o blob
            raise

    @staticmethod
    def get_blob_multipage_ken(bucket_name, directory, mat):
        """
            função identica a get_blob_multipage, diferença é que considera apenas as imagens .ken
            :param bucket_name:
            :param directory:
            :param mat:
            :return:
            """

        try:
            blobs = [bucket_name.blob(blob_name='IMG' + '/' + directory + '/' + f'{mat}.ken'),
                     bucket_name.blob(blob_name='IMG' + '/' + directory + '/' + f'{mat}.KEN')]

            blob_retornado = None
            for blob in blobs:
                if blob.exists():
                    blob.reload()  # Recarrega as propriedades do blob. Sem chamar essa função o GCP não me manda as infos.
                    if blob_retornado is None or blob.time_created > blob_retornado.time_created:
                        blob_retornado = blob

            return blob_retornado

        except (ValueError, KeyError, DefaultCredentialsError, RefreshError, NotFound) as e:
            print(f"O seguinte erro ocorreu: {e}")
            # retorno falso em caso de alguma exceção ao pegar o blob
            raise

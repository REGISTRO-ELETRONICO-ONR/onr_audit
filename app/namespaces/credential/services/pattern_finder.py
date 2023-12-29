import json
import os
from app.namespaces.credential.services.gcp_info import GCPInfo
from app.namespaces.credential.dataclasses import FinderData


class PatternFinder:
    """
    Classe para descobrir qual o padrão do CNS especifico
    Se o padrão for encontrado, a função gera um arquivo pattern.json na raíz do projeto informando qual o padrão.
    """

    def __init__(self, gcp_info: GCPInfo):
        self.gcp_info = gcp_info

    @staticmethod
    def _generate_pattern_file(pattern):
        with open("pattern.json", 'w') as fp:
            json.dump({"pattern": pattern}, fp)

    def _padrao_adois(self, data: FinderData):
        # CNS 112623

        project_id = data.project_id
        matricula = data.matricula
        cnm = data.cnm

        matricula = str(matricula).zfill(8)
        directory = str(int(int(matricula) / 1000) * 1000).zfill(8)

        bucket = self.gcp_info.get_bucket(project_id)
        blob = self.gcp_info.get_blob_multipage_ken(bucket, directory, matricula)
        if blob:
            pattern = 2
            self._generate_pattern_file(pattern)
            return True
        else:
            # se não tiver tento a chamada com o cnm
            blob = self.gcp_info.get_blob_multipage_ken(bucket, directory, cnm.replace("-", "").replace(".", ""))
            if blob:
                pattern = 2
                self._generate_pattern_file(pattern)
                return True
            else:
                return False

    def _padrao_btres(self, data: FinderData):
        # CNS 112599, 145557

        project_id = data.project_id
        matricula = data.matricula
        cnm = data.cnm

        matricula = str(matricula).zfill(8)
        directory = str(int(int(matricula) / 1000) * 1000).zfill(8)

        bucket = self.gcp_info.get_bucket(project_id)
        blob = self.gcp_info.get_blob_multipage(bucket, directory, matricula)
        if blob:
            pattern = 3
            self._generate_pattern_file(pattern)
            return True
        else:
            # se não tiver tento a chamada com o cnm
            blob = self.gcp_info.get_blob_multipage(bucket, directory, cnm.replace("-", "").replace(".", ""))
            if blob:
                pattern = 3
                self._generate_pattern_file(pattern)
                return True
            else:
                return False

    def _padrao_cquatro(self, data: FinderData):
        # 111179, 112482

        project_id = data.project_id
        matricula = data.matricula
        cnm = data.cnm

        matricula = str(matricula).zfill(8)
        directory = str(int(int(matricula) / 1000)).zfill(5) if ((int(matricula) / 1000) - int(
            (int(matricula) / 1000))) < 0.5 \
            else str(int(int(matricula) / 1000) + 1).zfill(5)

        bucket = self.gcp_info.get_bucket(project_id)
        blob = self.gcp_info.get_blob_multipage(bucket, directory, matricula)
        if blob:
            pattern = 4
            self._generate_pattern_file(pattern)
            return True
        else:
            # se não tiver tento a chamada com o cnm
            blob = self.gcp_info.get_blob_multipage(bucket, directory, cnm.replace("-", "").replace(".", ""))
            if blob:
                pattern = 4
                self._generate_pattern_file(pattern)
                return True
            else:
                return False

    # SEM TESTE
    def _padrao_dseis(self, data: FinderData):
        project_id = data.project_id
        matricula = data.matricula
        cnm = data.cnm

        matricula = str(matricula).zfill(8)
        directory = str(int(int(matricula) / 100000) + 1).ljust(6, '0')

        bucket = self.gcp_info.get_bucket(project_id)
        blob = self.gcp_info.get_blob_multipage(bucket, directory, matricula)
        if blob:
            pattern = 6
            self._generate_pattern_file(pattern)
            return True
        else:
            # se não tiver tento a chamada com o cnm
            blob = self.gcp_info.get_blob_multipage(bucket, directory, cnm.replace("-", "").replace(".", ""))
            if blob:
                pattern = 6
                self._generate_pattern_file(pattern)
                return True
            else:
                return False

    def _padrao_edoze(self, data: FinderData):
        # CNS 121004

        project_id = data.project_id
        matricula = data.matricula
        cnm = data.cnm

        matricula = str(matricula).zfill(8)
        directory = str(int(int(matricula) / 1000)).zfill(8)

        bucket = self.gcp_info.get_bucket(project_id)
        blob = self.gcp_info.get_blob_multipage(bucket, directory, matricula)
        if blob:
            pattern = 12
            self._generate_pattern_file(pattern)
            return True
        else:
            # se não tiver tento a chamada com o cnm
            blob = self.gcp_info.get_blob_multipage(bucket, directory, cnm.replace("-", "").replace(".", ""))
            if blob:
                pattern = 12
                self._generate_pattern_file(pattern)
                return True
            else:
                return False

    # SEM TESTE
    def _padrao_ftreze(self, data: FinderData):
        project_id = data.project_id
        matricula = data.matricula
        cnm = data.cnm

        matricula = str(matricula).zfill(8)
        directory = str(int(int(matricula) / 1000)).zfill(5)

        bucket = self.gcp_info.get_bucket(project_id)
        blob = self.gcp_info.get_blob_multipage(bucket, directory, matricula)
        if blob:
            pattern = 13
            self._generate_pattern_file(pattern)
            return True
        else:
            # se não tiver tento a chamada com o cnm
            blob = self.gcp_info.get_blob_multipage(bucket, directory, cnm.replace("-", "").replace(".", ""))
            if blob:
                pattern = 13
                self._generate_pattern_file(pattern)
                return True
            else:
                return False

    def _padrao_g_oito(self, data: FinderData):
        # 111252

        project_id = data.project_id
        matricula = data.matricula
        cnm = data.cnm

        matricula = str(matricula).zfill(6)
        directory = f'{str(int(int(matricula) / 1000)).zfill(3)}/{matricula}'
        bucket = self.gcp_info.get_bucket(project_id)
        blobs, get_image = self.gcp_info.get_blobs_and_image(bucket, directory, matricula)
        blobs = list(blobs)
        # retorno False se não houve retorno

        if not blobs:
            # caso não tenha, tento também com cnm
            blobs, get_image = self.gcp_info.get_blobs_and_image(bucket, directory, cnm.replace("-", "").replace(".", ""))
            blobs = list(blobs)
            if not blobs:
                return False

        # filtro pra tratar a questão de gif e GIF pro padrão 8
        pattern = 8
        self._generate_pattern_file(pattern)

        return True

    def _padrao_g_oito_v2(self, data: FinderData):
        # 111252

        project_id = data.project_id
        matricula = data.matricula
        cnm = data.cnm

        matricula = str(matricula).zfill(6)
        directory = f'{str(int(int(matricula) / 10000)).zfill(2).ljust(3, "0")}/{matricula}'

        bucket = self.gcp_info.get_bucket(project_id)
        blobs, get_image = self.gcp_info.get_blobs_and_image(bucket, directory, matricula)

        blobs = list(blobs)
        # retorno False se não houve retorno

        if not blobs:
            # caso não tenha, tento também com cnm
            blobs, get_image = self.gcp_info.get_blobs_and_image(bucket, directory, cnm.replace("-", "").replace(".", ""))
            blobs = list(blobs)
            if not blobs:
                return False

        pattern = 8
        self._generate_pattern_file(pattern)

        return True

    def _padrao_hsete(self, data: FinderData):
        # CNS 111138

        project_id = data.project_id
        mat = data.matricula
        cnm = data.cnm
        matricula = mat

        directory = str(int(int(mat) / 1000)).zfill(4)
        mat = str(mat).zfill(6).ljust(7, '0')

        bucket = self.gcp_info.get_bucket(project_id)
        blobs, get_image = self.gcp_info.get_blobs_and_image(bucket, directory, mat)

        blobs = list(blobs)

        # retorno False se não houve retorno
        if not blobs:
            # caso não tenha, tento também com cnm
            blobs, get_image = self.gcp_info.get_blobs_and_image(bucket, directory, cnm.replace("-", "").replace(".", ""))
            blobs = list(blobs)
            if not blobs:
                return False

        pattern = 7
        self._generate_pattern_file(pattern)

        return True

    # Serve para o padrao um também
    def _padrao_icatorze(self, data: FinderData):
        # 024588, 120329

        project_id = data.project_id
        matricula = data.matricula
        cnm = data.cnm

        matricula = str(matricula).zfill(6)
        directory = str(int(int(matricula) / 1000)).zfill(4)

        bucket = self.gcp_info.get_bucket(project_id)
        blobs, get_image = self.gcp_info.get_blobs_and_image(bucket, directory, matricula)

        blobs = list(blobs)
        # retorno False se não houve retorno
        if not blobs:
            # caso não tenha, tento também com cnm
            blobs, get_image = self.gcp_info.get_blobs_and_image(bucket, directory, cnm.replace("-", "").replace(".", ""))
            blobs = list(blobs)
            if not blobs:
                return False

        pattern = 14
        self._generate_pattern_file(pattern)

        return True

    def _padrao_kquinze(self, data: FinderData):
        # CNS 039073, 085183, 160028
        project_id = data.project_id
        matricula = data.matricula
        cnm = data.cnm

        matricula = str(matricula).zfill(8)
        directory = str(int(int(matricula) / 1000)).zfill(8)

        bucket = self.gcp_info.get_bucket(project_id)
        blobs, get_image = self.gcp_info.get_blobs_and_image(bucket, directory, matricula)

        blobs = list(blobs)
        # retorno False se não houve retorno
        if not blobs:
            # caso não tenha, tento também com cnm
            blobs, get_image = self.gcp_info.get_blobs_and_image(bucket, directory, cnm.replace("-", "").replace(".", ""))
            blobs = list(blobs)
            if not blobs:
                return False

        pattern = 15
        self._generate_pattern_file(pattern)

        return True

    def _padrao_l_onze(self, data: FinderData):
        # 111450
        project_id = data.project_id
        matricula = data.matricula
        cnm = data.cnm
        mat = matricula

        mat = str(mat).zfill(6)
        directory = str(int(int(mat) / 1000)).zfill(6)

        bucket_name = self.gcp_info.get_bucket(project_id)
        blobs, get_image = self.gcp_info.get_blobs_and_image(bucket_name, directory, mat)

        blobs = list(blobs)

        # retorno False se não houve retorno
        if not blobs:
            # caso não tenha, tento também com cnm
            blobs, get_image = self.gcp_info.get_blobs_and_image(bucket_name, directory, cnm.replace("-", "").replace(".", ""))
            blobs = list(blobs)
            if not blobs:
                return False

        pattern = 11
        self._generate_pattern_file(pattern)

        return True

    def _padrao_mcinco(self, data: FinderData):
        # 158055, 119636

        project_id = data.project_id
        matricula = data.matricula
        cnm = data.cnm

        matricula = str(matricula).zfill(8)
        directory = f"{int(int(matricula) / 500) * 500 if int(int(matricula) / 500) * 500 != 0 else 1}" \
                    f" a {(int(int(matricula) / 500) + 1) * 500 - 1}"

        bucket = self.gcp_info.get_bucket(project_id)
        blobs, get_image = self.gcp_info.get_blobs_and_image(bucket, directory, matricula)

        # o objeto blobs so da para ser percorrido uma unica vez, desta forma é necessário transforma-lo em lista primeiro.
        blobs = list(blobs)

        # retorno False se não houve retorno
        if not blobs:
            # caso não tenha, tento também com cnm
            blobs, get_image = self.gcp_info.get_blobs_and_image(bucket, directory, cnm.replace("-", "").replace(".", ""))
            blobs = list(blobs)
            if not blobs:
                return False

        pattern = 5
        self._generate_pattern_file(pattern)

        return True

    def _padrao_n_nove(self, data: FinderData):
        # CNS 058594

        project_id = data.project_id
        matricula = data.matricula
        cnm = data.cnm

        matricula = str(matricula).zfill(6)
        directory = str(int(int(matricula) / 1000)).zfill(3)

        bucket = self.gcp_info.get_bucket(project_id)
        blobs, get_image = self.gcp_info.get_blobs_and_image(bucket, directory, matricula)

        blobs = list(blobs)
        # retorno False se não houve retorno0.
        if not blobs:
            # caso não tenha, tento também com cnm
            blobs, get_image = self.gcp_info.get_blobs_and_image(bucket, directory, cnm.replace("-", "").replace(".", ""))
            blobs = list(blobs)
            if not blobs:
                return False

        pattern = 9
        self._generate_pattern_file(pattern)

        return True

    def _padrao_o_dezessete(self, data: FinderData):
        # 122218

        project_id = data.project_id
        matricula = data.matricula
        cnm = data.cnm

        directory = str(int(int(matricula) / 100)).ljust(len(str(matricula)), '0').zfill(6)
        matricula = f"{str(matricula).zfill(6)}20"

        bucket_name = self.gcp_info.get_bucket(project_id)
        blobs, get_image = self.gcp_info.get_blobs_and_image(bucket_name, directory, matricula)

        blobs = list(blobs)

        # retorno False se não houve retorno0.
        if not blobs:
            # caso não tenha, tento também com cnm
            blobs, get_image = self.gcp_info.get_blobs_and_image(bucket_name, directory, cnm.replace("-", "").replace(".", ""))
            blobs = list(blobs)
            if not blobs:
                return False

        pattern = 17
        self._generate_pattern_file(pattern)

        return True

    # serve para o padrao dezoito e dezesseis
    def _padrao_pdezoito(self, data: FinderData):
        # 088583; 163121; 038976; 093344

        project_id = data.project_id
        matricula = data.matricula
        cnm = data.cnm

        directory = str(int(int(matricula) / 1000)).zfill(3)
        matricula = matricula[-3:].zfill(3)

        bucket_name = self.gcp_info.get_bucket(project_id)
        blobs, get_image = self.gcp_info.get_blobs_and_image(bucket_name, directory, matricula)

        blobs = list(blobs)

        # retorno False se não houve retorno0.
        if not blobs:
            # caso não tenha, tento também com cnm
            blobs, get_image = self.gcp_info.get_blobs_and_image(bucket_name, directory, cnm.replace("-", "").replace(".", ""))
            blobs = list(blobs)
            if not blobs:
                return False

        pattern = 18
        self._generate_pattern_file(pattern)

        return True

    def find_image(self, data: FinderData) -> object:
        """
        função que corre por todas as funções de padrão que estão inclusas nesse módulo.
        As funções de padrões, são funções que dado determinado padrão define se existe uma matrícula no bucket do
        CNS(cartório)

        Caso a matrícula existe, a própria função que achou a matricula dará continuidade e finalizará o processamento do
        pdf chamando outras funções.


        :param data: objeto data que é uma dataclass FinderData
        :return:
        """

        ignore_list = ["find_image", "get_blobs_and_image", "get_blob_multipage", "get_blob_multipage_ken",
                                 "SQLAlchemyError", "Pedido", "Credential", "_filtro_tif", "_filtro_gif",
                                 "_handle_image_multitiff", "_handle_image_tiff", "DefaultCredentialsError",
                                 "RefreshError", "_create_folder", "generate_path",
                                 "NotFound", "get_bucket", "__init__", "_generate_pattern_file"]

        methods = [getattr(self, method_name) for method_name in dir(self)
                   if callable(getattr(self, method_name)) and not method_name.startswith("__")]

        for method in methods:
            print(method.__name__)
            if method.__name__ in ignore_list:
                continue  # pula a chamada recursiva à própria função e as funções importadas

            result = method(data)

            if result:
                print("funcao retornou True, encerrando loop")
                return True

        return False

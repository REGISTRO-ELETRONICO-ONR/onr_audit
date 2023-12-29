import json
from app.helpers.exceptions import PatternNotDefined


class GetMatriculaByPattern:

    @staticmethod
    def pattern_multitif_general(text: str) -> int:
        matricula = text.split("/")[-1].replace(".KEN", "").replace(".TIFF", "").replace(".tiff", "").replace(".ken", "").replace(".TIF", "").replace(".tif", "")
        if "." not in matricula and "-" not in matricula:  # ou seja, não é um cnm
            return int(matricula)

        matricula = matricula.split(".")[-1].split("-")[0]
        return int(matricula)

    @staticmethod
    def pattern_eight(text: str) -> int:
        matricula = text.split("/")[-1]
        if matricula.count("-") == 1:  # ou seja, não tá usando cnm
            matricula = matricula.split("-")[0]
            return int(matricula)
        else:
            matricula = matricula.replace(".gif", "").replace(".GIF", "").split(".")[-1].split("-")[0]
            return int(matricula)

    @staticmethod
    def pattern_seven_eleven_fifteen_seventeen(text: str) -> int:
        matricula = text.split("/")[-1]
        if matricula.count(".") == 1:  # ou seja, não tá usando cnm
            matricula = matricula.split(".")[0]
            return int(matricula)
        else:
            matricula = matricula.split(".")[-2].split("-")[0]
            return int(matricula)

    @staticmethod
    def pattern_fourteen(text: str) -> int:
        matricula = text.split("/")[-1].replace(".TIFF", "").replace(".tiff", "").replace(".TIF", "").replace(".tif", "")
        if matricula.count("-") == 1:  # ou seja, não tá usando cnm
            matricula = matricula.split(".")[0]
            return int(matricula)
        else:
            matricula = matricula.split(".")[-2].split("-")[0]
            return int(matricula)

    @staticmethod
    def pattern_sixteen_eighteen(text: str) -> int:
        matricula = text.replace(".TIFF", "").replace(".tiff", "").replace(".TIF", "").replace(".tif", "")
        osplit = matricula.split("/")
        matricula = ''.join(osplit[-2:])
        if matricula.count(".") == 0:
            matricula = ''.join([char for char in matricula if char.isdigit()])
            return int(matricula)
        else:
            matricula = matricula.split(".")[-1].split("-")[0]
            return int(matricula)

    @staticmethod
    def pattern_five(text: str) -> int:
        matricula = text.replace(".TIFF", "").replace(".tiff", "").replace(".TIF", "").replace(".tif", "")
        matricula = matricula.split("_")[0]
        if matricula.count(".") == 0:
            matricula = ''.join([char for char in matricula if char.isdigit()])
            return int(matricula)
        else:
            matricula = matricula.split(".")[-1].split("-")[0]
            return int(matricula)

    @staticmethod
    def get_pattern():
        with open('pattern.json', 'r') as file:
            pattern_dict = json.load(file)

        print(pattern_dict.get("pattern"))

        if not pattern_dict:
            raise PatternNotDefined

        return pattern_dict.get("pattern")


class GetMatricula:

    def __init__(self, get_matricula_by_pattern: GetMatriculaByPattern):
        self.get_matricula_by_pattern = get_matricula_by_pattern

    def get(self, text: str) -> int:

        pattern = self.get_matricula_by_pattern.get_pattern()

        if pattern in (2, 3, 4, 6, 12, 13):
            return self.get_matricula_by_pattern.pattern_multitif_general(text)
        elif pattern in (7, 11, 15, 17):
            return self.get_matricula_by_pattern.pattern_seven_eleven_fifteen_seventeen(text)
        elif pattern in (16, 18):
            return self.get_matricula_by_pattern.pattern_sixteen_eighteen(text)
        elif pattern == 8:
            return self.get_matricula_by_pattern.pattern_eight(text)
        elif pattern == 5:
            return self.get_matricula_by_pattern.pattern_five(text)
        else:
            return self.get_matricula_by_pattern.pattern_fourteen(text)

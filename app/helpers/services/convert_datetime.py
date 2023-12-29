import datetime


class ConvertDatetime:

    @staticmethod
    def convert_to_str(lista: list[dict]) -> list[dict]:
        for item in lista:
            item['date_request'] = str(item['date_request'])

        return lista

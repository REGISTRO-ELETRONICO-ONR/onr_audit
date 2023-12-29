from app.helpers.repositories.interfaces import GetLogsInterface
from app.helpers.models.pedidos import Pedidos
from datetime import datetime, date
import pytz


class RecordsDb(GetLogsInterface):

    @staticmethod
    def get(initial_date: date, finish_date: date, document: str = None) -> list:
        """
        Método para pegar todos os registros nesse intervalo de filtro determinado, onde documento é apenas opcional
        :param initial_date:
        :param finish_date:
        :param document:
        :return:
        """

        saopaulo = pytz.timezone('America/Sao_Paulo')

        # Criação dos datetime "aware" para São Paulo
        initial_date_aware = saopaulo.localize(datetime(initial_date.year, initial_date.month, initial_date.day, 0, 0))
        finish_date_aware = saopaulo.localize(datetime(finish_date.year, finish_date.month, finish_date.day, 23, 59, 59))

        # Convertendo os datetime para UTC e tornando-os "naive"
        initial_date_naive_utc = initial_date_aware.astimezone(pytz.UTC).replace(tzinfo=None)
        finish_date_naive_utc = finish_date_aware.astimezone(pytz.UTC).replace(tzinfo=None)

        new_query = Pedidos.query(Pedidos.date_request >= initial_date_naive_utc,
                                  Pedidos.date_request <= finish_date_naive_utc)
        if document:
            new_query = new_query.filter(Pedidos.document == document)

        records = new_query.fetch()
        print(records)

        return records

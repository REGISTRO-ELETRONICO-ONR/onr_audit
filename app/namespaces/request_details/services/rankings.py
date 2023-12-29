import datetime

from app.helpers.dataclasses import DatastoreData
from collections import Counter
import pytz


class Ranking:
    """
    Classe para tratar a logica por trás de cada um dos rankings solicitados nos endpoints
    """

    def __init__(self, records: list[DatastoreData], quantity: int):
        self.records = records
        self.quantity = quantity
        # Tornar o datetime "aware" usando UTC
        self.utc = pytz.UTC
        self.sao_paulo = pytz.timezone('America/Sao_Paulo')

    def ranking_documento(self, paid: bool):
        # Conta quantas vezes cada CPF aparece na lista
        if paid:
            counter = Counter([item.document for item in self.records if item.value])
        else:
            counter = Counter([item.document for item in self.records if not item.value])

        # Cria um dicionário para mapear CPFs a nomes
        map_document_name = {item.document: item.name for item in self.records}

        # Organiza os CPFs em ordem decrescente de aparições
        ordered_documents = sorted(counter.keys(), key=lambda cpf: (-counter[cpf], cpf))
        print(ordered_documents)

        # Cria a lista de saída com os CPFs e suas respectivas posições
        final_exit = [{"document": cpf,
                       "name": map_document_name[cpf],
                       "quantity": counter[cpf],
                       "position": idx + 1} for idx, cpf in enumerate(ordered_documents)]

        if len(final_exit) > self.quantity:
            return final_exit[:self.quantity]
        else:
            return final_exit

    def ranking_ip_onr_apps(self):

        # Conta quantas vezes cada CPF aparece na lista
        counter = Counter([item.ip for item in self.records])

        # Organiza os CPFs em ordem decrescente de aparições
        ordered_ips = sorted(counter.keys(), key=lambda ip: (-counter[ip], ip))
        print(ordered_ips)

        # Cria a lista de saída com os CPFs e suas respectivas posições
        final_exit = [{"ip": ip,
                       "quantity": counter[ip],
                       "position": idx + 1} for idx, ip in enumerate(ordered_ips)]

        print(final_exit)

        if len(final_exit) > self.quantity:
            return final_exit[:self.quantity]
        else:
            return final_exit

    def ranking_client_ip(self, paid: bool):

        # Conta quantas vezes cada CPF aparece na lista
        if paid:
            counter = Counter([item.ip_cliente for item in self.records if item.value])
        else:
            counter = Counter([item.ip_cliente for item in self.records if not item.value])

        # Organiza os CPFs em ordem decrescente de aparições
        ordered_ips = sorted(counter.keys(), key=lambda ip: (-counter[ip], ip))
        print(ordered_ips)

        # Cria a lista de saída com os CPFs e suas respectivas posições
        final_exit = [{"ip": ip_cliente,
                       "quantity": counter[ip_cliente],
                       "position": idx + 1} for idx, ip_cliente in enumerate(ordered_ips)]

        print(final_exit)

        if len(final_exit) > self.quantity:
            return final_exit[:self.quantity]
        else:
            return final_exit

    def ranking_documento_fds(self, paid: bool):
        # Conta quantas vezes cada CPF aparece na lista

        self.records = [item for item in self.records if item.date_request.weekday() in (5, 6)]

        if paid:
            contador = Counter([item.document for item in self.records if item.value])
        else:
            contador = Counter([item.document for item in self.records if not item.value])

        # Cria um dicionário para mapear CPFs a nomes
        map_document_name = {item.document: item.name for item in self.records}

        # Organiza os CPFs em ordem decrescente de aparições
        ordered_documents = sorted(contador.keys(), key=lambda cpf: (-contador[cpf], cpf))
        print(ordered_documents)

        # Cria a lista de saída com os CPFs e suas respectivas posições
        final_exit = [{"document": cpf,
                       "name": map_document_name[cpf],
                       "quantity": contador[cpf],
                       "position": idx + 1} for idx, cpf in enumerate(ordered_documents)]

        if len(final_exit) > self.quantity:
            return final_exit[:self.quantity]
        else:
            return final_exit

    def ranking_documento_motive(self):
        # Trago apenas os casos gratis
        print(len(self.records), "ANTES")
        self.records = [record for record in self.records if not record.value and record.motivo]
        print(len(self.records), "DEPOIS")
        # Conta quantas vezes cada CPF aparece na lista
        contador = Counter([item.motivo for item in self.records])

        # Organiza os CPFs em ordem decrescente de aparições
        motive_ordered = sorted(contador.keys(), key=lambda motive: (-contador[motive], motive))
        print(motive_ordered)

        # Cria a lista de saída com os CPFs e suas respectivas posições
        final_exit = [{"motive": motive,
                       "quantity": contador[motive],
                       "position": idx + 1} for idx, motive in enumerate(motive_ordered)]

        if len(final_exit) > self.quantity:
            return final_exit[:self.quantity]
        else:
            return final_exit

    def ranking_documento_same_minuto(self, paid: bool):
        if paid:
            self.records = [record for record in self.records if record.value]
        else:
            self.records = [record for record in self.records if not record.value]

        # Usa a função definida abaixo
        counter = self._count_downloads_within_same_minute(self.records)

        ranking_list = [{"document": cpf,
                         "name": self.records[i].name,
                         "quantity": count,
                         "start_time": self.utc.localize(self.records[i].date_request)
                             .astimezone(self.sao_paulo).strftime('%Y-%m-%d %H:%M:%S')}
                        for i, downloads in counter.items()
                        for cpf, count in downloads.items()]

        ordered_ranking = sorted(ranking_list, key=lambda x: (-x["quantity"], x["document"]))
        print(ordered_ranking)

        for idx, entry in enumerate(ordered_ranking):
            entry["position"] = idx + 1

        if len(ordered_ranking) > self.quantity:
            return ordered_ranking[:self.quantity]
        else:
            return ordered_ranking

    @staticmethod
    def _count_downloads_within_same_minute(records):
        from collections import defaultdict
        # Primeiro, ordena os registros pela data
        records.sort(key=lambda x: x.date_request)

        contador = defaultdict(lambda: defaultdict(int))  # utilizo quando preciso acessar/gerar um dado que não existe

        for idx, record in enumerate(records):
            start_time = record.date_request
            finish_time = start_time + datetime.timedelta(minutes=1)

            for inner_records in records:

                if start_time <= inner_records.date_request < finish_time and inner_records.document == record.document:
                    contador[idx][record.document] += 1

        return contador

    def ranking_sequence(self, paid: bool):

        if paid:
            self.records = [record for record in self.records if record.value]
        else:
            self.records = [record for record in self.records if not record.value]

        lista_ordenada = sorted(self.records, key=lambda x: x.number)
        inicio_sequencia = lista_ordenada[0].number
        fim_sequencia = inicio_sequencia
        sequencias = []

        for i in range(len(lista_ordenada) - 1):
            diferenca = lista_ordenada[i + 1].number - lista_ordenada[i].number
            if diferenca == 1:
                fim_sequencia = lista_ordenada[i + 1].number
            elif diferenca == 0:
                pass  # Ignorar matrículas duplicadas
            else:
                # apenas sequencias maiores que 10
                if fim_sequencia - inicio_sequencia > 10:
                    sequencias.append({"begin_sequence": inicio_sequencia,
                                       "end_sequence": fim_sequencia,
                                       "size_sequence": fim_sequencia - inicio_sequencia + 1})
                inicio_sequencia = lista_ordenada[i + 1].number
                fim_sequencia = inicio_sequencia

        if fim_sequencia - inicio_sequencia > 10:
            sequencias.append({"begin_sequence": inicio_sequencia,
                               "end_sequence": fim_sequencia,
                               "size_sequence": fim_sequencia - inicio_sequencia + 1})

        sequencias.sort(key=lambda x: x["size_sequence"], reverse=True)

        # rankeando sequencia
        for position, item in enumerate(sequencias, start=1):
            item["position"] = position

        if len(sequencias) > self.quantity:
            return sequencias[:self.quantity]
        else:
            return sequencias

    def sequence_details(self, begin_sequence, end_sequence, paid: bool):

        if paid:
            self.records = [record for record in self.records if record.value]
        else:
            self.records = [record for record in self.records if not record.value]

        self.records = sorted(self.records, key=lambda x: x.number)

        sequencia = [{"document": record.document,
                      "name": record.name,
                      "number": record.number,
                      "ip_client": record.ip_cliente,
                      "motive": record.motivo,
                      "value": record.value,
                      "date_request": self.utc.localize(record.date_request)
                          .astimezone(self.sao_paulo).strftime('%Y-%m-%d %H:%M:%S')}
                     for record in self.records if begin_sequence <= record.number <= end_sequence]

        return sequencia

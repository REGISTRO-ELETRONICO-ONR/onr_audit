import stdnum.iso7064.mod_97_10


class CNM:

    def create(self, cns: str, number: int) -> str:
        """
            função simples que gera o cnm dado o cns e a matricula
            :param cns:
            :param number: matricula
            :return:
            """

        matricula = str(number).zfill(7)
        livro = 2
        pre_cnm = cns + str(livro) + matricula
        get_cnm = self._calc_mod_97_base_10(pre_cnm)

        return get_cnm[2]

    @staticmethod
    def _calc_mod_97_base_10(num):
        dig_verificador = stdnum.iso7064.mod_97_10.calc_check_digits(num)
        cnm = str(num) + str(dig_verificador)
        cns = cnm[0:6]
        livro = cnm[6]
        matricula = cnm[7:14]
        matricula_cnm = cns + '.' + livro + '.' + matricula + '-' + dig_verificador

        return cns, matricula, matricula_cnm

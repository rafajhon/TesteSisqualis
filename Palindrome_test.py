
import unittest

from palindrome import (valida_entrada, encontra_palindromo_mais_proximo,
                        zerar_palindrome, proximo_palindrome,
                        proximo_palindrome_simples,
                        proximo_palindrome_composto)


class TestaPalindromeMaior(unittest.TestCase):
    def test_validado_caso_entrada_nula(self):
        self.assertEqual(False, valida_entrada(''))

    def test_validando_caso_entrada_seja_nao_algarismo(self):
        self.assertEqual(False, valida_entrada('seffr@$@'))

    def test_validando_caso_seja_entrada_valida(self):
        self.assertEqual(True, valida_entrada('5232'))

    def teste_entra_palindrome_com_uma_mudanca(self):
        self.assertEqual(encontra_palindromo_mais_proximo('431'), '434')

    def teste_mudaca_em_toda_metade_do_numeoro(self):
        self.assertEqual(encontra_palindromo_mais_proximo('156478'), '156651')

    def teste_encontra_palindrome_maior(self):
        self.assertEqual(encontra_palindromo_mais_proximo('9523'), '9559')

    def teste_encotra_palindrome_menor(self):
        self.assertEqual(encontra_palindromo_mais_proximo('1234567'),
                         '1234321')

    def teste_entrora_o_proximo_palimedro_com_palindromes_conhecidos_1(self):
        self.assertEqual(proximo_palindrome_simples('523325'), '524425')

    def teste_entrora_o_proximo_palimedro_com_palindromes_conhecidos_2(self):
        self.assertEqual(proximo_palindrome_simples('2112'), '2222')

    def teste_entrora_o_proximo_palimedro_com_palindromes_conhecidos_3(self):
        self.assertEqual(proximo_palindrome_simples('989'), '999')

    def teste_entrora_o_proximo_palimedro_com_palindromes_conhecidos_4(self):
        self.assertEqual(proximo_palindrome_simples('1458541'), '1459541')

    def test_achar_proximo_palindrome_com_tres_casas_decimais(self):
        self.assertEqual(proximo_palindrome_composto('00'), '101')

    def test_achar_proximo_palindrome_com_quato_casas_decimais(self):
        self.assertEqual(proximo_palindrome_composto('000'), '1001')

    def test_achar_proximo_palindrome_com_cinco_casas_decimais(self):
        self.assertEqual(proximo_palindrome_composto('0000'), '10001')

    def test_achar_proximo_palindrome_com_seis_casas_decimais(self):
        self.assertEqual(proximo_palindrome_composto('00000'), '100001')

    def test_achar_proximo_palindrome_com_oito_casas_decimais(self):
        self.assertEqual(proximo_palindrome_composto('0000000'), '10000001')

    def teste_funcao_proximo_palindrome_palindromes_conhecidos_1(self):
        self.assertEqual(proximo_palindrome('808'), '909')

    def teste_funcao_proximo_palindrome_palindromes_conhecidos_2(self):
        self.assertEqual(proximo_palindrome('210012'), '220022')

    def teste_funcao_proximo_palindrome_palindromes_conhecidos_3(self):
        self.assertEqual(proximo_palindrome('88088'), '89098')

    def teste_funcao_proximo_palindrome_palindromes_conhecidos_4(self):
        self.assertEqual(proximo_palindrome('10001'), '20002')

    def teste_zerando_tres_algarismo_nove(self):
        self.assertEqual(zerar_palindrome('999'), '000')

    def teste_zerando_dois_algarismo_nove(self):
        self.assertEqual(zerar_palindrome('1991'), '1001')

    def teste_zerando_sete_algarismo_nove(self):
        self.assertEqual(zerar_palindrome('9999999'), '0000000')

unittest.main()

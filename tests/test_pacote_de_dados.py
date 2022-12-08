import pytest
from ProtocoloDeComunicacao.pacote_de_dados import PacoteDeDados
from pytest import mark

class TestClass:

    def test_quando_instanciar_5_pacotes_o_quinto_pacote_deve_ter_indice_5(self):
        # Given (Contexto)
        # NA

        # When (Ação)
        pacote_1 = PacoteDeDados()
        pacote_2 = PacoteDeDados()
        pacote_3 = PacoteDeDados()
        pacote_4 = PacoteDeDados()
        pacote_5 = PacoteDeDados()

        # Then (Desfecho)
        indice_esperado = 5
        assert pacote_5.get_indice()

    def test_template(self):
        # Given (Contexto)
        # When (Ação)
        # Then (Desfecho)
        pass
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
        indice_recebido = pacote_5.get_indice()

        # Then (Desfecho)
        indice_esperado = 5
        assert indice_recebido == indice_esperado


    def test_quando_instanciar_pacote_tamanho_do_pacote_deve_ter_valor_0(self):
        # Given (Contexto)
        # NA

        # When (Ação)
        pacote = PacoteDeDados()
        tamanho_recebido = pacote.get_tamanho()

        # Then (Desfecho)
        tamanho_esperado = 0
        assert tamanho_recebido == tamanho_esperado


    def test_quando_instanciar_pacote_qtd_de_dados_deve_ter_valor_0(self):
        # Given (Contexto)
        # NA

        # When (Ação)
        pacote = PacoteDeDados()
        qtd_de_dados_recebido = pacote.get_quantidade_de_dados()

        # Then (Desfecho)
        qtd_de_dados_esperado = 0
        assert qtd_de_dados_recebido == qtd_de_dados_esperado


    def test_quando_instanciar_pacote_inicializador_1_deve_ter_valor_1_negativo(self):
        # Given (Contexto)
        # NA

        # When (Ação)
        pacote = PacoteDeDados()
        inicializador_1_recebido = pacote.get_inicializador_1()

        # Then (Desfecho)
        inicializador_1_esperado = -1
        assert inicializador_1_recebido == inicializador_1_esperado


    def test_quando_instanciar_pacote_inicializador_2_deve_ter_valor_1_negativo(self):
        # Given (Contexto)
        # NA

        # When (Ação)
        pacote = PacoteDeDados()
        inicializador_2_recebido = pacote.get_inicializador_2()

        # Then (Desfecho)
        inicializador_2_esperado = -1
        assert inicializador_2_recebido == inicializador_2_esperado


    def test_quando_instanciar_pacote_comando_deve_ter_valor_1_negativo(self):
        # Given (Contexto)
        # NA

        # When (Ação)
        pacote = PacoteDeDados()
        comando_recebido = pacote.get_comando()

        # Then (Desfecho)
        comando_esperado = -1
        assert comando_recebido == comando_esperado


    def test_quando_instanciar_pacote_a_lista_dados_deve_estar_vazia(self):
        # Given (Contexto)
        # NA

        # When (Ação)
        pacote = PacoteDeDados()
        tamanho_da_lista_dados_recebido = len(pacote.get_dados())

        # Then (Desfecho)
        tamanho_da_lista_dados_esperado = 0
        assert tamanho_da_lista_dados_recebido == tamanho_da_lista_dados_esperado


    def test_quando_instanciar_pacote_a_lista_pacote_deve_estar_vazia(self):
        # Given (Contexto)
        # NA

        # When (Ação)
        pacote = PacoteDeDados()
        tamanho_da_lista_pacote_recebido = len(pacote.get_pacote())

        # Then (Desfecho)
        tamanho_da_lista_pacote_esperado = 0
        assert tamanho_da_lista_pacote_recebido == tamanho_da_lista_pacote_esperado


    def test_quando_instanciar_pacote_crc8_deve_ter_valor_1_negativo(self):
        # Given (Contexto)
        # NA

        # When (Ação)
        pacote = PacoteDeDados()
        crc8_recebido = pacote.get_crc8()

        # Then (Desfecho)
        crc8_esperado = -1
        assert crc8_recebido == crc8_esperado


    def test_quando_instanciar_pacote_esta_valido_deve_ter_valor_false(self):
        # Given (Contexto)
        # NA

        # When (Ação)
        pacote = PacoteDeDados()
        esta_valido_recebido = pacote.esta_valido()

        # Then (Desfecho)
        esta_valido_esperado = False
        assert esta_valido_recebido == esta_valido_esperado


    def test_quando_set_inicializador_1_recebe_string_deve_retornar_type_error(self):
        with pytest.raises(TypeError):
            # Given (Contexto)
            inicializador_1_entrada = "0xAA"

            # When (Ação)
            pacote = PacoteDeDados()
            pacote.set_inicializador_1(inicializador_1_entrada)

            # Then (Desfecho)
            assert TypeError()


    def test_quando_set_inicializador_1_recebe_float_deve_retornar_type_error(self):
        with pytest.raises(TypeError):
            # Given (Contexto)
            inicializador_1_entrada = 0.25

            # When (Ação)
            pacote = PacoteDeDados()
            pacote.set_inicializador_1(inicializador_1_entrada)

            # Then (Desfecho)
            assert TypeError()


    def test_quando_set_inicializador_1_recebe_lista_deve_retornar_type_error(self):
        with pytest.raises(TypeError):
            # Given (Contexto)
            inicializador_1_entrada = []

            # When (Ação)
            pacote = PacoteDeDados()
            pacote.set_inicializador_1(inicializador_1_entrada)

            # Then (Desfecho)
            assert TypeError()


    def test_quando_set_inicializador_1_recebe_tupla_deve_retornar_type_error(self):
        with pytest.raises(TypeError):
            # Given (Contexto)
            inicializador_1_entrada = ()

            # When (Ação)
            pacote = PacoteDeDados()
            pacote.set_inicializador_1(inicializador_1_entrada)

            # Then (Desfecho)
            assert TypeError()


    def test_quando_set_inicializador_1_recebe_int_menor_que_0_deve_retornar_value_error(self):
        with pytest.raises(ValueError):
            # Given (Contexto)
            inicializador_1_entrada = -1

            # When (Ação)
            pacote = PacoteDeDados()
            pacote.set_inicializador_1(inicializador_1_entrada)

            # Then (Desfecho)
            assert ValueError()


    def test_quando_set_inicializador_1_recebe_int_maior_que_255_deve_retornar_value_error(self):
        with pytest.raises(ValueError):
            # Given (Contexto)
            inicializador_1_entrada = 256

            # When (Ação)
            pacote = PacoteDeDados()
            pacote.set_inicializador_1(inicializador_1_entrada)

            # Then (Desfecho)
            assert ValueError()


    def test_quando_set_inicializador_1_recebe_1_deve_armazenar_1(self):
        # Given (Contexto)
        inicializador_1_entrada = 1

        # When (Ação)
        pacote = PacoteDeDados()
        pacote.set_inicializador_1(inicializador_1_entrada)
        inicializador_1_armazenado = pacote.get_inicializador_1()

        # Then (Desfecho)
        inicializador_1_esperado = 1
        assert inicializador_1_armazenado == inicializador_1_esperado


    def test_quando_set_inicializador_1_recebe_255_deve_armazenar_255(self):
        # Given (Contexto)
        inicializador_1_entrada = 255

        # When (Ação)
        pacote = PacoteDeDados()
        pacote.set_inicializador_1(inicializador_1_entrada)
        inicializador_1_armazenado = pacote.get_inicializador_1()

        # Then (Desfecho)
        inicializador_1_esperado = 255
        assert inicializador_1_armazenado == inicializador_1_esperado


    def test_quando_set_inicializador_2_recebe_string_deve_retornar_type_error(self):
        with pytest.raises(TypeError):
            # Given (Contexto)
            inicializador_2_entrada = "0xAA"

            # When (Ação)
            pacote = PacoteDeDados()
            pacote.set_inicializador_2(inicializador_2_entrada)

            # Then (Desfecho)
            assert TypeError()


    def test_quando_set_inicializador_2_recebe_float_deve_retornar_type_error(self):
        with pytest.raises(TypeError):
            # Given (Contexto)
            inicializador_2_entrada = 0.25

            # When (Ação)
            pacote = PacoteDeDados()
            pacote.set_inicializador_2(inicializador_2_entrada)

            # Then (Desfecho)
            assert TypeError()


    def test_quando_set_inicializador_2_recebe_lista_deve_retornar_type_error(self):
        with pytest.raises(TypeError):
            # Given (Contexto)
            inicializador_2_entrada = []

            # When (Ação)
            pacote = PacoteDeDados()
            pacote.set_inicializador_2(inicializador_2_entrada)

            # Then (Desfecho)
            assert TypeError()


    def test_quando_set_inicializador_2_recebe_tupla_deve_retornar_type_error(self):
        with pytest.raises(TypeError):
            # Given (Contexto)
            inicializador_2_entrada = ()

            # When (Ação)
            pacote = PacoteDeDados()
            pacote.set_inicializador_2(inicializador_2_entrada)

            # Then (Desfecho)
            assert TypeError()


    def test_quando_set_inicializador_2_recebe_int_menor_que_0_deve_retornar_value_error(self):
        with pytest.raises(ValueError):
            # Given (Contexto)
            inicializador_2_entrada = -1

            # When (Ação)
            pacote = PacoteDeDados()
            pacote.set_inicializador_2(inicializador_2_entrada)

            # Then (Desfecho)
            assert ValueError()


    def test_quando_set_inicializador_2_recebe_int_maior_que_255_deve_retornar_value_error(self):
        with pytest.raises(ValueError):
            # Given (Contexto)
            inicializador_2_entrada = 256

            # When (Ação)
            pacote = PacoteDeDados()
            pacote.set_inicializador_2(inicializador_2_entrada)

            # Then (Desfecho)
            assert ValueError()


    def test_quando_set_inicializador_2_recebe_1_deve_armazenar_1(self):
        # Given (Contexto)
        inicializador_2_entrada = 1

        # When (Ação)
        pacote = PacoteDeDados()
        pacote.set_inicializador_2(inicializador_2_entrada)
        inicializador_2_armazenado = pacote.get_inicializador_2()

        # Then (Desfecho)
        inicializador_2_esperado = 1
        assert inicializador_2_armazenado == inicializador_2_esperado


    def test_quando_set_inicializador_2_recebe_255_deve_armazenar_255(self):
        # Given (Contexto)
        inicializador_2_entrada = 255

        # When (Ação)
        pacote = PacoteDeDados()
        pacote.set_inicializador_2(inicializador_2_entrada)
        inicializador_2_armazenado = pacote.get_inicializador_2()

        # Then (Desfecho)
        inicializador_2_esperado = 255
        assert inicializador_2_armazenado == inicializador_2_esperado









    def test_quando_set_comando_recebe_string_deve_retornar_type_error(self):
        with pytest.raises(TypeError):
            # Given (Contexto)
            comando_entrada = "0xAA"

            # When (Ação)
            pacote = PacoteDeDados()
            pacote.set_comando(comando_entrada)

            # Then (Desfecho)
            assert TypeError()


    def test_quando_set_comando_recebe_float_deve_retornar_type_error(self):
        with pytest.raises(TypeError):
            # Given (Contexto)
            comando_entrada = 0.25

            # When (Ação)
            pacote = PacoteDeDados()
            pacote.set_comando(comando_entrada)

            # Then (Desfecho)
            assert TypeError()


    def test_quando_set_comando_recebe_lista_deve_retornar_type_error(self):
        with pytest.raises(TypeError):
            # Given (Contexto)
            comando_entrada = []

            # When (Ação)
            pacote = PacoteDeDados()
            pacote.set_comando(comando_entrada)

            # Then (Desfecho)
            assert TypeError()


    def test_quando_set_comando_recebe_tupla_deve_retornar_type_error(self):
        with pytest.raises(TypeError):
            # Given (Contexto)
            comando_entrada = ()

            # When (Ação)
            pacote = PacoteDeDados()
            pacote.set_comando(comando_entrada)

            # Then (Desfecho)
            assert TypeError()


    def test_quando_set_comando_recebe_int_menor_que_1_deve_retornar_value_error(self):
        with pytest.raises(ValueError):
            # Given (Contexto)
            comando_entrada = 0

            # When (Ação)
            pacote = PacoteDeDados()
            pacote.set_comando(comando_entrada)

            # Then (Desfecho)
            assert ValueError()


    def test_quando_set_comando_recebe_int_maior_que_254_deve_retornar_value_error(self):
        with pytest.raises(ValueError):
            # Given (Contexto)
            comando_entrada = 255

            # When (Ação)
            pacote = PacoteDeDados()
            pacote.set_comando(comando_entrada)

            # Then (Desfecho)
            assert ValueError()


    def test_quando_set_comando_recebe_1_deve_armazenar_1(self):
        # Given (Contexto)
        comando_entrada = 1

        # When (Ação)
        pacote = PacoteDeDados()
        pacote.set_comando(comando_entrada)
        comando_armazenado = pacote.get_comando()

        # Then (Desfecho)
        comando_esperado = 1
        assert comando_armazenado == comando_esperado


    def test_quando_set_comando_recebe_254_deve_armazenar_254(self):
        # Given (Contexto)
        comando_entrada = 254

        # When (Ação)
        pacote = PacoteDeDados()
        pacote.set_comando(comando_entrada)
        comando_armazenado = pacote.get_comando()

        # Then (Desfecho)
        comando_esperado = 254
        assert comando_armazenado == comando_esperado


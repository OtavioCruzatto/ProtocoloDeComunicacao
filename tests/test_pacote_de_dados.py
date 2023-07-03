import pytest
from ProtocoloDeComunicacao.pacote_de_dados import PacoteDeDados
from pytest import fixture
from pytest import mark

class TestClass:


    @fixture
    def pacote(self):

        # SetUp
        # print("\nBloco executado antes de cada teste!")

        # Exercise and Assert
        yield PacoteDeDados()

        # TearDown
        # print("\nBloco executado após cada teste!")
        del self


    def test_quando_instanciar_5_pacotes_e_destruir_3_a_quantidade_de_pacotes_deve_ser_2(self):
        # Given
        # NA

        # When
        pacote_1 = PacoteDeDados()
        pacote_2 = PacoteDeDados()
        pacote_3 = PacoteDeDados()
        pacote_4 = PacoteDeDados()
        pacote_5 = PacoteDeDados()
        del pacote_1
        del pacote_2
        del pacote_3
        quantidade_de_pacotes_recebido = PacoteDeDados.get_quantidade_de_pacotes()
        del pacote_4
        del pacote_5

        # Then
        quantidade_de_pacotes_esperado = 2
        assert quantidade_de_pacotes_recebido == quantidade_de_pacotes_esperado


    def test_quando_instanciar_pacote_tamanho_do_pacote_deve_ter_valor_0(self, pacote):
        # Given
        # NA

        # When
        tamanho_recebido = pacote.get_tamanho()

        # Then
        tamanho_esperado = 0
        assert tamanho_recebido == tamanho_esperado


    def test_quando_instanciar_pacote_qtd_de_dados_deve_ter_valor_0(self, pacote):
        # Given
        # NA

        # When
        qtd_de_dados_recebido = pacote.get_quantidade_de_dados()

        # Then
        qtd_de_dados_esperado = 0
        assert qtd_de_dados_recebido == qtd_de_dados_esperado


    def test_quando_instanciar_pacote_inicializador_1_deve_ter_valor_1_negativo(self, pacote):
        # Given
        # NA

        # When
        inicializador_1_recebido = pacote.get_inicializador_1()

        # Then
        inicializador_1_esperado = -1
        assert inicializador_1_recebido == inicializador_1_esperado


    def test_quando_instanciar_pacote_inicializador_2_deve_ter_valor_1_negativo(self, pacote):
        # Given
        # NA

        # When
        inicializador_2_recebido = pacote.get_inicializador_2()

        # Then
        inicializador_2_esperado = -1
        assert inicializador_2_recebido == inicializador_2_esperado


    def test_quando_instanciar_pacote_comando_deve_ter_valor_1_negativo(self, pacote):
        # Given
        # NA

        # When
        comando_recebido = pacote.get_comando()

        # Then
        comando_esperado = -1
        assert comando_recebido == comando_esperado


    def test_quando_instanciar_pacote_a_lista_dados_deve_estar_vazia(self, pacote):
        # Given
        # NA

        # When
        tamanho_da_lista_dados_recebido = len(pacote.get_dados())

        # Then
        tamanho_da_lista_dados_esperado = 0
        assert tamanho_da_lista_dados_recebido == tamanho_da_lista_dados_esperado


    def test_quando_instanciar_pacote_a_lista_pacote_deve_estar_vazia(self, pacote):
        # Given
        # NA

        # When
        tamanho_da_lista_pacote_recebido = len(pacote.get_pacote())

        # Then
        tamanho_da_lista_pacote_esperado = 0
        assert tamanho_da_lista_pacote_recebido == tamanho_da_lista_pacote_esperado


    def test_quando_instanciar_pacote_crc8_deve_ter_valor_1_negativo(self, pacote):
        # Given
        # NA

        # When
        crc8_recebido = pacote.get_crc8()

        # Then
        crc8_esperado = -1
        assert crc8_recebido == crc8_esperado


    def test_quando_instanciar_pacote_esta_valido_deve_ter_valor_false(self, pacote):
        # Given
        # NA

        # When
        esta_valido_recebido = pacote.esta_valido()

        # Then
        esta_valido_esperado = False
        assert esta_valido_recebido == esta_valido_esperado


    def test_quando_set_inicializador_1_recebe_string_deve_retornar_type_error(self, pacote):
        with pytest.raises(TypeError):
            # Given
            inicializador_1_entrada = "0xAA"

            # When
            pacote.set_inicializador_1(inicializador_1_entrada)

            # Then
            assert TypeError()


    def test_quando_set_inicializador_1_recebe_float_deve_retornar_type_error(self, pacote):
        with pytest.raises(TypeError):
            # Given
            inicializador_1_entrada = 0.25

            # When
            pacote.set_inicializador_1(inicializador_1_entrada)

            # Then
            assert TypeError()


    def test_quando_set_inicializador_1_recebe_lista_deve_retornar_type_error(self, pacote):
        with pytest.raises(TypeError):
            # Given
            inicializador_1_entrada = []

            # When
            pacote.set_inicializador_1(inicializador_1_entrada)

            # Then
            assert TypeError()


    def test_quando_set_inicializador_1_recebe_tupla_deve_retornar_type_error(self, pacote):
        with pytest.raises(TypeError):
            # Given
            inicializador_1_entrada = ()

            # When
            pacote.set_inicializador_1(inicializador_1_entrada)

            # Then
            assert TypeError()


    def test_quando_set_inicializador_1_recebe_int_menor_que_0_deve_retornar_value_error(self, pacote):
        with pytest.raises(ValueError):
            # Given
            inicializador_1_entrada = -1

            # When
            pacote.set_inicializador_1(inicializador_1_entrada)

            # Then
            assert ValueError()


    def test_quando_set_inicializador_1_recebe_int_maior_que_255_deve_retornar_value_error(self, pacote):
        with pytest.raises(ValueError):
            # Given
            inicializador_1_entrada = 256

            # When
            pacote.set_inicializador_1(inicializador_1_entrada)

            # Then
            assert ValueError()


    def test_quando_set_inicializador_1_recebe_1_deve_armazenar_1(self, pacote):
        # Given
        inicializador_1_entrada = 1

        # When
        pacote.set_inicializador_1(inicializador_1_entrada)
        inicializador_1_armazenado = pacote.get_inicializador_1()

        # Then
        inicializador_1_esperado = 1
        assert inicializador_1_armazenado == inicializador_1_esperado


    def test_quando_set_inicializador_1_recebe_255_deve_armazenar_255(self, pacote):
        # Given
        inicializador_1_entrada = 255

        # When
        pacote.set_inicializador_1(inicializador_1_entrada)
        inicializador_1_armazenado = pacote.get_inicializador_1()

        # Then
        inicializador_1_esperado = 255
        assert inicializador_1_armazenado == inicializador_1_esperado


    def test_quando_set_inicializador_2_recebe_string_deve_retornar_type_error(self, pacote):
        with pytest.raises(TypeError):
            # Given
            inicializador_2_entrada = "0xAA"

            # When
            pacote.set_inicializador_2(inicializador_2_entrada)

            # Then
            assert TypeError()


    def test_quando_set_inicializador_2_recebe_float_deve_retornar_type_error(self, pacote):
        with pytest.raises(TypeError):
            # Given
            inicializador_2_entrada = 0.25

            # When
            pacote.set_inicializador_2(inicializador_2_entrada)

            # Then
            assert TypeError()


    def test_quando_set_inicializador_2_recebe_lista_deve_retornar_type_error(self, pacote):
        with pytest.raises(TypeError):
            # Given
            inicializador_2_entrada = []

            # When
            pacote.set_inicializador_2(inicializador_2_entrada)

            # Then
            assert TypeError()


    def test_quando_set_inicializador_2_recebe_tupla_deve_retornar_type_error(self, pacote):
        with pytest.raises(TypeError):
            # Given
            inicializador_2_entrada = ()

            # When
            pacote.set_inicializador_2(inicializador_2_entrada)

            # Then
            assert TypeError()


    def test_quando_set_inicializador_2_recebe_int_menor_que_0_deve_retornar_value_error(self, pacote):
        with pytest.raises(ValueError):
            # Given
            inicializador_2_entrada = -1

            # When
            pacote.set_inicializador_2(inicializador_2_entrada)

            # Then
            assert ValueError()


    def test_quando_set_inicializador_2_recebe_int_maior_que_255_deve_retornar_value_error(self, pacote):
        with pytest.raises(ValueError):
            # Given
            inicializador_2_entrada = 256

            # When
            pacote.set_inicializador_2(inicializador_2_entrada)

            # Then
            assert ValueError()


    def test_quando_set_inicializador_2_recebe_1_deve_armazenar_1(self, pacote):
        # Given
        inicializador_2_entrada = 1

        # When
        pacote.set_inicializador_2(inicializador_2_entrada)
        inicializador_2_armazenado = pacote.get_inicializador_2()

        # Then
        inicializador_2_esperado = 1
        assert inicializador_2_armazenado == inicializador_2_esperado


    def test_quando_set_inicializador_2_recebe_255_deve_armazenar_255(self, pacote):
        # Given
        inicializador_2_entrada = 255

        # When
        pacote.set_inicializador_2(inicializador_2_entrada)
        inicializador_2_armazenado = pacote.get_inicializador_2()

        # Then
        inicializador_2_esperado = 255
        assert inicializador_2_armazenado == inicializador_2_esperado


    def test_quando_set_comando_recebe_string_deve_retornar_type_error(self, pacote):
        with pytest.raises(TypeError):
            # Given
            comando_entrada = "0xAA"

            # When
            pacote.set_comando(comando_entrada)

            # Then
            assert TypeError()


    def test_quando_set_comando_recebe_float_deve_retornar_type_error(self, pacote):
        with pytest.raises(TypeError):
            # Given
            comando_entrada = 0.25

            # When
            pacote.set_comando(comando_entrada)

            # Then
            assert TypeError()


    def test_quando_set_comando_recebe_lista_deve_retornar_type_error(self, pacote):
        with pytest.raises(TypeError):
            # Given
            comando_entrada = []

            # When
            pacote.set_comando(comando_entrada)

            # Then
            assert TypeError()


    def test_quando_set_comando_recebe_tupla_deve_retornar_type_error(self, pacote):
        with pytest.raises(TypeError):
            # Given
            comando_entrada = ()

            # When
            pacote.set_comando(comando_entrada)

            # Then
            assert TypeError()


    def test_quando_set_comando_recebe_int_menor_que_1_deve_retornar_value_error(self, pacote):
        with pytest.raises(ValueError):
            # Given
            comando_entrada = 0

            # When
            pacote.set_comando(comando_entrada)

            # Then
            assert ValueError()


    def test_quando_set_comando_recebe_int_maior_que_254_deve_retornar_value_error(self, pacote):
        with pytest.raises(ValueError):
            # Given
            comando_entrada = 255

            # When
            pacote.set_comando(comando_entrada)

            # Then
            assert ValueError()


    def test_quando_set_comando_recebe_1_deve_armazenar_1(self, pacote):
        # Given
        comando_entrada = 1

        # When
        pacote.set_comando(comando_entrada)
        comando_armazenado = pacote.get_comando()

        # Then
        comando_esperado = 1
        assert comando_armazenado == comando_esperado


    def test_quando_set_comando_recebe_254_deve_armazenar_254(self, pacote):
        # Given
        comando_entrada = 254

        # When
        pacote.set_comando(comando_entrada)
        comando_armazenado = pacote.get_comando()

        # Then
        comando_esperado = 254
        assert comando_armazenado == comando_esperado


    def test_quando_atualizar_for_chamado_sem_setar_inicializador_1_deve_retornar_value_error(self, pacote):
        with pytest.raises(ValueError):
            # Given
            inicializador_2 = 0x55
            comando = 0x02

            # When
            pacote.set_inicializador_2(inicializador_2)
            pacote.set_comando(comando)
            pacote.atualizar()

            # Then
            assert ValueError()


    def test_quando_atualizar_for_chamado_sem_setar_inicializador_2_deve_retornar_value_error(self, pacote):
        with pytest.raises(ValueError):
            # Given
            inicializador_1 = 0x55
            comando = 0x02

            # When
            pacote.set_inicializador_1(inicializador_1)
            pacote.set_comando(comando)
            pacote.atualizar()

            # Then
            assert ValueError()


    def test_quando_atualizar_for_chamado_sem_setar_comando_deve_retornar_value_error(self, pacote):
        with pytest.raises(ValueError):
            # Given
            inicializador_1 = 0x55
            inicializador_2 = 0xaa

            # When
            pacote.set_inicializador_1(inicializador_1)
            pacote.set_inicializador_2(inicializador_2)
            pacote.atualizar()

            # Then
            assert ValueError()


    def test_quando_atualizar_for_chamado_com_inicializadores_comando_e_sem_dados_deve_montar_o_pacote(self, pacote):
        # Given
        inicializador_1 = 0xaa
        inicializador_2 = 0x55
        comando = 0x7f

        # When
        pacote.set_inicializador_1(inicializador_1)
        pacote.set_inicializador_2(inicializador_2)
        pacote.set_comando(comando)
        pacote.atualizar()
        pacote_montado = pacote.get_pacote()

        # Then
        pacote_esperado = [0xaa, 0x55, 0x7f, 0x00, 0xe6]
        assert pacote_montado == pacote_esperado


    def test_quando_atualizar_for_chamado_com_inicializadores_comando_e_sem_dados_o_pacote_deve_ter_tamanho_5(self, pacote):
        # Given
        inicializador_1 = 0xaa
        inicializador_2 = 0x55
        comando = 0x7f

        # When
        pacote.set_inicializador_1(inicializador_1)
        pacote.set_inicializador_2(inicializador_2)
        pacote.set_comando(comando)
        pacote.atualizar()
        tamanho_pacote_montado = pacote.get_tamanho()

        # Then
        tamanho_pacote_esperado = 5
        assert tamanho_pacote_montado == tamanho_pacote_esperado


    def test_quando_atualizar_for_chamado_com_inicializadores_comando_e_sem_dados_a_qtd_de_dados_deve_ser_0(self, pacote):
        # Given
        inicializador_1 = 0xaa
        inicializador_2 = 0x55
        comando = 0x7f

        # When
        pacote.set_inicializador_1(inicializador_1)
        pacote.set_inicializador_2(inicializador_2)
        pacote.set_comando(comando)
        pacote.atualizar()
        qtd_dados_no_pacote = pacote.get_quantidade_de_dados()

        # Then
        qtd_dados_esperados = 0
        assert qtd_dados_no_pacote == qtd_dados_esperados


    def test_quando_atualizar_for_chamado_com_inicializadores_comando_e_sem_dados_o_pacote_deve_ser_valido(self, pacote):
        # Given
        inicializador_1 = 0xaa
        inicializador_2 = 0x55
        comando = 0x7f

        # When
        pacote.set_inicializador_1(inicializador_1)
        pacote.set_inicializador_2(inicializador_2)
        pacote.set_comando(comando)
        pacote.atualizar()
        pacote_montado_valido = pacote.esta_valido()

        # Then
        pacote_esperado_valido = True
        assert pacote_montado_valido == pacote_esperado_valido


    def test_quando_atualizar_for_chamado_com_inicializadores_comando_e_com_dados_deve_montar_o_pacote(self, pacote):
        # Given
        inicializador_1 = 0xaa
        inicializador_2 = 0x55
        comando = 0x7f
        dados = [0x70, 0xb4, 0xf7, 0x03, 0x68]

        # When
        pacote.set_inicializador_1(inicializador_1)
        pacote.set_inicializador_2(inicializador_2)
        pacote.set_comando(comando)
        pacote.set_dados(dados)
        pacote.atualizar()
        pacote_montado = pacote.get_pacote()

        # Then
        pacote_esperado = [0xaa, 0x55, 0x7f, 0x05, 0x70, 0xb4, 0xf7, 0x03, 0x68, 0xf9]
        assert pacote_montado == pacote_esperado


    def test_quando_atualizar_for_chamado_com_inicializadores_comando_e_com_dados_o_pacote_deve_ter_tamanho_10(self, pacote):
        # Given
        inicializador_1 = 0xaa
        inicializador_2 = 0x55
        comando = 0x7f
        dados = [0x70, 0xb4, 0xf7, 0x03, 0x68]

        # When
        pacote.set_inicializador_1(inicializador_1)
        pacote.set_inicializador_2(inicializador_2)
        pacote.set_comando(comando)
        pacote.set_dados(dados)
        pacote.atualizar()
        tamanho_pacote_montado = pacote.get_tamanho()

        # Then
        tamanho_pacote_esperado = 10
        assert tamanho_pacote_montado == tamanho_pacote_esperado


    def test_quando_atualizar_for_chamado_com_inicializadores_comando_e_com_dados_a_qtd_de_dados_deve_ser_5(self, pacote):
        # Given
        inicializador_1 = 0xaa
        inicializador_2 = 0x55
        comando = 0x7f
        dados = [0x70, 0xb4, 0xf7, 0x03, 0x68]

        # When
        pacote.set_inicializador_1(inicializador_1)
        pacote.set_inicializador_2(inicializador_2)
        pacote.set_comando(comando)
        pacote.set_dados(dados)
        pacote.atualizar()
        qtd_dados_no_pacote = pacote.get_quantidade_de_dados()

        # Then
        qtd_dados_esperados = 5
        assert qtd_dados_no_pacote == qtd_dados_esperados


    def test_quando_atualizar_for_chamado_com_inicializadores_comando_e_com_dados_o_pacote_deve_ser_valido(self, pacote):
        # Given
        inicializador_1 = 0xaa
        inicializador_2 = 0x55
        comando = 0x7f
        dados = [0x70, 0xb4, 0xf7, 0x03, 0x68]

        # When
        pacote.set_inicializador_1(inicializador_1)
        pacote.set_inicializador_2(inicializador_2)
        pacote.set_comando(comando)
        pacote.set_dados(dados)
        pacote.atualizar()
        pacote_montado_valido = pacote.esta_valido()

        # Then
        pacote_esperado_valido = True
        assert pacote_montado_valido == pacote_esperado_valido


    def test_quando_set_dados_recebe_string_deve_retornar_type_error(self, pacote):
        with pytest.raises(TypeError):
            # Given
            dados_entrada = "[0x79, 0x56, 0x46]"

            # When
            pacote.set_dados(dados_entrada)

            # Then
            assert TypeError()


    def test_quando_set_dados_recebe_int_deve_retornar_type_error(self, pacote):
        with pytest.raises(TypeError):
            # Given
            dados_entrada = 0x79

            # When
            pacote.set_dados(dados_entrada)

            # Then
            assert TypeError()


    def test_quando_set_dados_recebe_float_deve_retornar_type_error(self, pacote):
        with pytest.raises(TypeError):
            # Given
            dados_entrada = 12.5

            # When
            pacote.set_dados(dados_entrada)

            # Then
            assert TypeError()


    def test_quando_set_dados_recebe_uma_lista_com_256_elementos_deve_retornar_value_error(self, pacote):
        with pytest.raises(ValueError):
            # Given
            dados_entrada = [0xaa for _ in range(256)]

            # When
            pacote.set_dados(dados_entrada)

            # Then
            assert ValueError()


    def test_quando_set_dados_recebe_uma_lista_contendo_uma_string_deve_retornar_type_error(self, pacote):
        with pytest.raises(TypeError):
            # Given
            dados_entrada = [0xaa, 0x55, 0xf7, 0xff, "0x53", 0x56]

            # When
            pacote.set_dados(dados_entrada)

            # Then
            assert TypeError()


    def test_quando_set_dados_recebe_uma_lista_contendo_um_float_deve_retornar_type_error(self, pacote):
        with pytest.raises(TypeError):
            # Given
            dados_entrada = [0xaa, 0x55, 0xf7, 0xff, 53.4, 0x56]

            # When
            pacote.set_dados(dados_entrada)

            # Then
            assert TypeError()


    def test_quando_set_dados_recebe_uma_lista_contendo_uma_lista_deve_retornar_type_error(self, pacote):
        with pytest.raises(TypeError):
            # Given
            dados_entrada = [0xaa, 0x55, 0xf7, 0xff, [], 0x56]

            # When
            pacote.set_dados(dados_entrada)

            # Then
            assert TypeError()


    def test_quando_set_dados_recebe_uma_lista_contendo_uma_tupla_deve_retornar_type_error(self, pacote):
        with pytest.raises(TypeError):
            # Given
            dados_entrada = [0xaa, 0x55, 0xf7, 0xff, (), 0x56]

            # When
            pacote.set_dados(dados_entrada)

            # Then
            assert TypeError()


    def test_quando_set_dados_recebe_uma_lista_contendo_um_int_menor_que_0_deve_retornar_value_error(self, pacote):
        with pytest.raises(ValueError):
            # Given
            dados_entrada = [0xaa, 0x55, 0xf7, 0xff, -1, 0x56]

            # When
            pacote.set_dados(dados_entrada)

            # Then
            assert ValueError()


    def test_quando_set_dados_recebe_uma_lista_contendo_um_int_maior_que_255_deve_retornar_value_error(self, pacote):
        with pytest.raises(ValueError):
            # Given
            dados_entrada = [0xaa, 0x55, 0xf7, 0xff, 256, 0x56]

            # When
            pacote.set_dados(dados_entrada)

            # Then
            assert ValueError()


    def test_quando_set_dados_recebe_uma_lista_valida_de_6_elementos_deve_armazenar_os_6_elementos(self, pacote):
        # Given
        dados_entrada = [0xaa, 0x55, 0xf7, 0xff, 0x12, 0x56]

        # When
        pacote.set_dados(dados_entrada)
        dados_armazenados = pacote.get_dados()

        # Then
        dados_esperados = [0xaa, 0x55, 0xf7, 0xff, 0x12, 0x56]
        assert dados_armazenados == dados_esperados


    def test_quando_set_dados_recebe_uma_lista_valida_de_6_elementos_deve_setar_qtd_de_dados_com_6(self, pacote):
        # Given
        dados_entrada = [0xaa, 0x55, 0xf7, 0xff, 0x12, 0x56]

        # When
        pacote.set_dados(dados_entrada)
        qtd_dados_armazenados = pacote.get_quantidade_de_dados()

        # Then
        qtd_dados_esperados = 6
        assert qtd_dados_armazenados == qtd_dados_esperados


    def test_quando_montar_recebe_todos_os_parametros_validos_deve_armazenar_o_pacote(self, pacote):
        # Given
        inicializador_1 = 0xaa
        inicializador_2 = 0x55
        comando = 0x7f
        dados = [0x70, 0xb4, 0xf7, 0x03, 0x68]

        # When
        pacote.montar(inicializador_1, inicializador_2, comando, dados=dados)
        pacote_armazenado = pacote.get_pacote()

        # Then
        pacote_esperado = [0xaa, 0x55, 0x7f, 0x05, 0x70, 0xb4, 0xf7, 0x03, 0x68, 0xf9]
        assert pacote_armazenado == pacote_esperado


    def test_quando_montar_recebe_todos_os_parametros_validos_deve_apresentar_os_dados_como_string(self, pacote):
        # Given
        inicializador_1 = 0xaa
        inicializador_2 = 0x55
        comando = 0x7f
        dados = [0x70, 0xb4, 0xf7, 0x03, 0x68]

        # When
        pacote.montar(inicializador_1, inicializador_2, comando, dados=dados)
        apresentar_pacote_como_string = str(pacote)

        # Then
        string_esperada = (f"Status: Valido\n"
                            "Byte inicializador 1: 0xaa\n"
                            "Byte inicializador 2: 0x55\n"
                            "Qtd de bytes no pacote: 10\n"
                            "Qtd de bytes de dados: 5\n"
                            "Comando: 0x7f\n"
                            "CRC8 (Polinomio 0x07): 0xf9\n"
                            "Dados: ['0x70', '0xb4', '0xf7', '0x3', '0x68']\n"
                            "Pacote: ['0xaa', '0x55', '0x7f', '0x5', '0x70', '0xb4', '0xf7', '0x3', '0x68', '0xf9']\n")
        assert apresentar_pacote_como_string == string_esperada


    def test_quando_pacote_estiver_invalido_deve_apresentar_os_dados_como_string(self, pacote):
        # Given
        # NA

        # When
        apresentar_pacote_como_string = str(pacote)

        # Then
        string_esperada = (f"Status: Invalido\n"
                            "Byte inicializador 1: -0x1\n"
                            "Byte inicializador 2: -0x1\n"
                            "Qtd de bytes no pacote: 0\n"
                            "Qtd de bytes de dados: 0\n"
                            "Comando: -0x1\n"
                            "CRC8 (Polinomio 0x07): -0x1\n"
                            "Dados: []\n"
                            "Pacote: []\n")
        assert apresentar_pacote_como_string == string_esperada

    def test_quando_decodificar_receber_pacote_de_apenas_um_inteiro_deve_retornar_type_error(self, pacote):
        with pytest.raises(TypeError):
            # Given
            # NA

            # When
            pacote.decodificar(int(1))

            # Then
            assert TypeError()

    def test_quando_decodificar_receber_pacote_de_apenas_um_float_deve_retornar_type_error(self, pacote):
        with pytest.raises(TypeError):
            # Given
            # NA

            # When
            pacote.decodificar(float(1.5))

            # Then
            assert TypeError()

    def test_quando_decodificar_receber_pacote_de_apenas_um_char_deve_retornar_type_error(self, pacote):
        with pytest.raises(TypeError):
            # Given
            # NA

            # When
            pacote.decodificar("a")

            # Then
            assert TypeError()

    def test_quando_decodificar_receber_pacote_de_uma_string_deve_retornar_type_error(self, pacote):
        with pytest.raises(TypeError):
            # Given
            # NA

            # When
            pacote.decodificar("abcde")

            # Then
            assert TypeError()

    def test_quando_decodificar_receber_uma_lista_com_mais_de_260_elementos_deve_retornar_value_error(self, pacote):
        with pytest.raises(ValueError):
            # Given
            # NA

            # When
            pacote_a_ser_decodificado = [(int(i/2)) for i in range(261)]
            pacote.decodificar(pacote_a_ser_decodificado)

            # Then
            assert ValueError()

    def test_quando_decodificar_receber_uma_lista_com_menos_de_5_elementos_deve_retornar_value_error(self, pacote):
        with pytest.raises(ValueError):
            # Given
            # NA

            # When
            pacote_a_ser_decodificado = [(int(i)) for i in range(4)]
            pacote.decodificar(pacote_a_ser_decodificado)

            # Then
            assert ValueError()

    def test_quando_decodificar_receber_uma_lista_contendo_um_float_deve_retornar_value_error(self, pacote):
        with pytest.raises(ValueError):
            # Given
            # NA

            # When
            pacote_a_ser_decodificado = [5, 6, 7.5, 8 ,9]
            pacote.decodificar(pacote_a_ser_decodificado)

            # Then
            assert ValueError()

    def test_quando_decodificar_receber_uma_lista_contendo_um_char_deve_retornar_value_error(self, pacote):
        with pytest.raises(ValueError):
            # Given
            # NA

            # When
            pacote_a_ser_decodificado = [5, 6, "7", 8 ,9]
            pacote.decodificar(pacote_a_ser_decodificado)

            # Then
            assert ValueError()

    def test_quando_decodificar_receber_uma_lista_contendo_uma_string_deve_retornar_value_error(self, pacote):
        with pytest.raises(ValueError):
            # Given
            # NA

            # When
            pacote_a_ser_decodificado = [5, 6, "7567", 8 ,9]
            pacote.decodificar(pacote_a_ser_decodificado)

            # Then
            assert ValueError()

    def test_quando_decodificar_receber_uma_lista_contendo_um_valor_maior_que_255_deve_retornar_value_error(self, pacote):
        with pytest.raises(ValueError):
            # Given
            # NA

            # When
            pacote_a_ser_decodificado = [5, 6, 256, 8 ,9]
            pacote.decodificar(pacote_a_ser_decodificado)

            # Then
            assert ValueError()

    def test_quando_decodificar_receber_uma_lista_contendo_um_valor_menor_que_0_deve_retornar_value_error(self, pacote):
        with pytest.raises(ValueError):
            # Given
            # NA

            # When
            pacote_a_ser_decodificado = [5, 6, -1, 8 ,9]
            pacote.decodificar(pacote_a_ser_decodificado)

            # Then
            assert ValueError()

    def test_quando_decodificar_receber_uma_lista_com_crc8_invalido_deve_retornar_value_error(self, pacote):
        with pytest.raises(ValueError):
            # Given
            # NA

            # When
            pacote_a_ser_decodificado = [5, 6, 7, 8 ,9]
            pacote.decodificar(pacote_a_ser_decodificado)

            # Then
            assert ValueError()

    def test_quando_decodificar_receber_uma_lista_com_inicializador_1_0x31_o_byte_decodificado_deve_ser_0x31(self, pacote):
        # Given
        # NA

        # When
        pacote_a_ser_decodificado = [0x31, 0x32, 0x33, 0x05, 0x35, 0x36, 0x37, 0x38, 0x39, 0x78]
        pacote.decodificar(pacote_a_ser_decodificado)

        # Then
        byte_inicializador_1_esperado = 0x31
        byte_inicializador_1 = pacote.get_inicializador_1()
        assert byte_inicializador_1 == byte_inicializador_1_esperado

    def test_quando_decodificar_receber_uma_lista_com_inicializador_2_0x32_o_byte_decodificado_deve_ser_0x32(self, pacote):
        # Given
        # NA

        # When
        pacote_a_ser_decodificado = [0x31, 0x32, 0x33, 0x05, 0x35, 0x36, 0x37, 0x38, 0x39, 0x78]
        pacote.decodificar(pacote_a_ser_decodificado)

        # Then
        byte_inicializador_2_esperado = 0x32
        byte_inicializador_2 = pacote.get_inicializador_2()
        assert byte_inicializador_2 == byte_inicializador_2_esperado

    def test_quando_decodificar_receber_uma_lista_com_comando_0x33_o_byte_decodificado_deve_ser_0x33(self, pacote):
        # Given
        # NA

        # When
        pacote_a_ser_decodificado = [0x31, 0x32, 0x33, 0x05, 0x35, 0x36, 0x37, 0x38, 0x39, 0x78]
        pacote.decodificar(pacote_a_ser_decodificado)

        # Then
        comando_esperado = 0x33
        comando = pacote.get_comando()
        assert comando == comando_esperado

    def test_quando_decodificar_receber_uma_lista_com_crc8_0x78_o_byte_decodificado_deve_ser_0x78(self, pacote):
        # Given
        # NA

        # When
        pacote_a_ser_decodificado = [0x31, 0x32, 0x33, 0x05, 0x35, 0x36, 0x37, 0x38, 0x39, 0x78]
        pacote.decodificar(pacote_a_ser_decodificado)

        # Then
        crc8_esperado = 0x78
        crc8 = pacote.get_crc8()
        assert crc8 == crc8_esperado

    def test_quando_decodificar_receber_uma_lista_com_10_bytes_o_tamanho_do_pacote_deve_ser_10(self, pacote):
        # Given
        # NA

        # When
        pacote_a_ser_decodificado = [0x31, 0x32, 0x33, 0x05, 0x35, 0x36, 0x37, 0x38, 0x39, 0x78]
        pacote.decodificar(pacote_a_ser_decodificado)

        # Then
        tamanho_esperado = 10
        tamanho = pacote.get_tamanho()
        assert tamanho == tamanho_esperado

    def test_quando_decodificar_receber_uma_lista_com_a_qtd_de_bytes_de_dados_informada_incorreta_deve_retornar_value_error(self, pacote):
        with pytest.raises(ValueError):
            # Given
            # NA

            # When
            pacote_a_ser_decodificado = [0x31, 0x32, 0x33, 0x06, 0x35, 0x36, 0x37, 0x38, 0x39, 0x03]
            pacote.decodificar(pacote_a_ser_decodificado)

            # Then
            assert ValueError()

    def test_quando_decodificar_receber_um_pacote_valido_com_dados_deve_separar_os_dados(self, pacote):
        # Given
        # NA

        # When
        pacote_a_ser_decodificado = [0x31, 0x32, 0x33, 0x05, 0x35, 0x36, 0x37, 0x38, 0x39, 0x78]
        pacote.decodificar(pacote_a_ser_decodificado)

        # Then
        dados_esperados = [0x35, 0x36, 0x37, 0x38, 0x39]
        dados = pacote.get_dados()
        assert dados == dados_esperados

    def test_quando_decodificar_receber_um_pacote_valido_sem_dados_deve_nao_ter_os_dados(self, pacote):
        # Given
        # NA

        # When
        pacote_a_ser_decodificado = [0xAA, 0x55, 0x01, 0x00, 0x92]
        pacote.decodificar(pacote_a_ser_decodificado)

        # Then
        dados_esperados = []
        dados = pacote.get_dados()
        assert dados == dados_esperados


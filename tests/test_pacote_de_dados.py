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


    def test_quando_instanciar_5_pacotes_o_quinto_pacote_deve_ter_indice_5(self):
        # Given
        # NA

        # When
        pacote_1 = PacoteDeDados()
        pacote_2 = PacoteDeDados()
        pacote_3 = PacoteDeDados()
        pacote_4 = PacoteDeDados()
        pacote_5 = PacoteDeDados()
        indice_recebido = pacote_5.get_indice()
        del pacote_1
        del pacote_2
        del pacote_3
        del pacote_4
        del pacote_5

        # Then
        indice_esperado = 5
        assert indice_recebido == indice_esperado


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
        string_esperada = ( f"Pacote: 1\n"
                            "Status: Valido\n"
                            "Byte inicializador 1: 0xaa\n"
                            "Byte inicializador 2: 0x55\n"
                            "Qtd de bytes no pacote: 10\n"
                            "Qtd de bytes de dados: 5\n"
                            "Comando: 0x7f\n"
                            "CRC8 (Polinomio 0x07): 0xf9\n"
                            "Dados: ['0x70', '0xb4', '0xf7', '0x3', '0x68']\n"
                            "Pacote: ['0xaa', '0x55', '0x7f', '0x5', '0x70', '0xb4', '0xf7', '0x3', '0x68', '0xf9']\n")
        assert apresentar_pacote_como_string == string_esperada


    def test_quando_pacote_estives_invalido_deve_apresentar_os_dados_como_string(self, pacote):
        # Given
        # NA

        # When
        apresentar_pacote_como_string = str(pacote)

        # Then
        string_esperada = (f"Pacote: 1\n"
                            "Status: Invalido\n"
                            "Byte inicializador 1: -0x1\n"
                            "Byte inicializador 2: -0x1\n"
                            "Qtd de bytes no pacote: 0\n"
                            "Qtd de bytes de dados: 0\n"
                            "Comando: -0x1\n"
                            "CRC8 (Polinomio 0x07): -0x1\n"
                            "Dados: []\n"
                            "Pacote: []\n")
        assert apresentar_pacote_como_string == string_esperada

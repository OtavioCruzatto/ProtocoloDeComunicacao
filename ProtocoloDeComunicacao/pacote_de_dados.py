import crc8

class PacoteDeDados:
    quantidade_de_pacotes: int = 0

    def __init__(self, inicializador_1: int, inicializador_2: int, comando: int, dados: list[int] = []) -> None:
        self.__tamanho_do_pacote: int = 0
        self.__qtd_de_dados: int = 0

        self.__inicilizador_1: int = -1
        self.__inicilizador_2: int = -1
        self.__comando: int = -1
        self.__dados: list[int] = []
        self.__pacote_de_dados: list[int] = []
        self.__crc8: int = -1

        self.set_inicializador_1(inicializador_1)
        self.set_inicializador_2(inicializador_2)
        self.set_comando(comando)
        self.set_dados(dados)

        self.update_pacote_de_dados()
        PacoteDeDados.quantidade_de_pacotes += 1
        self.__indice_do_pacote: int = PacoteDeDados.quantidade_de_pacotes


    def __str__(self) -> str:
        return (f"Pacote: {self.__indice_do_pacote}.\nQuantidade de bytes: {len(self)}.\n"
                f"Quantidade de dados: {self.get_quantidade_de_dados()}.\nComando: {hex(self.get_comando())}.\n"
                f"CRC8 (Polinomio 0x07): {hex(self.__crc8)}.\nDados: {[hex(byte) for byte in self.__dados]}\n"
                f"Pacote: {[hex(byte) for byte in self.__pacote_de_dados]}\n")


    def __len__(self) -> int:
        return self.get_tamanho_do_pacote()


    def set_inicializador_1(self, inicializador_1: int) -> None:
        if (type(inicializador_1) is not int):
            raise TypeError("Variavel 'inicializador_1' deve ser do tipo int.")

        if (inicializador_1 < 0x00) or (inicializador_1 > 0xff):
            raise ValueError("Variavel 'inicializador_1' deve estar entre 0 (0x00) e 255 (0xff).")

        self.__inicilizador_1 = inicializador_1


    def get_inicializador_1(self) -> int:
        return self.__inicilizador_1


    def set_inicializador_2(self, inicializador_2: int) -> None:
        if (type(inicializador_2) is not int):
            raise TypeError("Variavel 'inicializador_2' deve ser do tipo int.")

        if (inicializador_2 < 0x00) or (inicializador_2 > 0xff):
            raise ValueError("Variavel 'inicializador_2' deve estar entre 0 (0x00) e 255 (0xff).")

        self.__inicilizador_2 = inicializador_2


    def get_inicializador_2(self) -> int:
        return self.__inicilizador_2


    def set_comando(self, comando: int) -> None:
        if (type(comando) is not int):
            raise TypeError("Variavel 'comando' deve ser do tipo int.")

        if (comando < 0x01) or (comando > 0xfe):
            raise ValueError("Variavel 'comando' deve estar entre 1 (0x01) e 254 (0xfe).")

        self.__comando = comando


    def get_comando(self) -> int:
        return self.__comando


    def get_pacote_de_dados(self) -> list[int]:
        return self.__pacote_de_dados


    def set_dados(self, dados: list[int]) -> None:
        if (type(dados) is not list):
            raise TypeError("Variavel 'dados' deve ser do tipo list.")

        if any(not isinstance(dado, int) for dado in dados):
            raise ValueError("Elementos da variavel 'dados' devem ser do tipo int.")

        if (len(dados) > 255):
            raise ValueError("Variavel 'dados' pode conter no maximo 255 elementos.")

        self.__dados = dados
        self.__qtd_de_dados = len(self.__dados)


    def update_pacote_de_dados(self) -> None:
        if (self.__inicilizador_1 == -1):
            raise ValueError("Variavel 'inicializador_1' nao definida.")

        if (self.__inicilizador_2 == -1):
            raise ValueError("Variavel 'inicializador_2' nao definida.")

        if (self.__comando == -1):
            raise ValueError("Variavel 'comando' nao definida.")

        self.__pacote_de_dados.clear()
        self.__pacote_de_dados.append(self.__inicilizador_1)
        self.__pacote_de_dados.append(self.__inicilizador_2)
        self.__pacote_de_dados.append(self.__comando)
        self.__pacote_de_dados.append(self.__qtd_de_dados)

        if (self.__qtd_de_dados != 0):
            for dado in self.__dados:
                self.__pacote_de_dados.append(dado)

        self.__calcular_crc8_polinomio_0x07()
        self.__pacote_de_dados.append(self.__crc8)
        self.__tamanho_do_pacote = len(self.__pacote_de_dados)


    def get_tamanho_do_pacote(self) -> int:
        return self.__tamanho_do_pacote


    def get_quantidade_de_dados(self) -> int:
        return self.__qtd_de_dados


    def __calcular_crc8_polinomio_0x07(self):
        crc_8 = crc8.crc8()
        pacote_de_dados_bytes = bytes(self.__pacote_de_dados)
        crc_8.update(pacote_de_dados_bytes)
        crc_8_calculado = int(crc_8.hexdigest(), 16)
        if (crc_8_calculado < 0) or (crc_8_calculado > 255):
            raise ValueError("Erro no calculo do CRC8")
        self.__crc8 = crc_8_calculado

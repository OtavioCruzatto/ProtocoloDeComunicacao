from ProtocoloDeComunicacao.pacote_de_dados import PacoteDeDados
from Comandos import Comandos

inicializador_1: int = 0xAA
inicializador_2: int = 0x55

pacote_1 = PacoteDeDados()
pacote_1.montar(inicializador_1, inicializador_2, Comandos.COMANDO_001.value)
print(pacote_1)

dados_para_montar_pacote: list[int] = [0x45, 0xa8, 0x05, 0x98, 0x67, 0x3b, 0xe4, 0xc5]
pacote_2 = PacoteDeDados()
pacote_2.montar(inicializador_1, inicializador_2, Comandos.COMANDO_002.value, dados=dados_para_montar_pacote)
print(pacote_2)

pacote_para_decodificar_com_dados: list[int] = [0x31, 0x32, 0x33, 0x05, 0x35, 0x36, 0x37, 0x38, 0x39, 0x78]
pacote_3 = PacoteDeDados()
pacote_3.decodificar(pacote_para_decodificar_com_dados)
print(pacote_3)

pacote_para_decodificar_sem_dados: list[int] = [0xaa, 0x55, 0x07, 0x00, 0xec]
pacote_4 = PacoteDeDados()
pacote_4.decodificar(pacote_para_decodificar_sem_dados)
print(pacote_4)

pacote_5 = PacoteDeDados()
print((pacote_5))

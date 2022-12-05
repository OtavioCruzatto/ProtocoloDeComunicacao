from ProtocoloDeComunicacao.pacote_de_dados import PacoteDeDados
from Comandos import Comandos

inicializador_1: int = 0xAA
inicializador_2: int = 0x55
dados: list[int] = [0x45, 0xa8, 0x05, 0x98, 0x67, 0x3b, 0xe4, 0xc5]

pacote_1 = PacoteDeDados(inicializador_1, inicializador_2, Comandos.COMANDO_001.value)
print(pacote_1)

pacote_2 = PacoteDeDados(inicializador_1, inicializador_2, Comandos.COMANDO_002.value, dados=dados)
print(pacote_2)









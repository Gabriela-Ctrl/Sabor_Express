from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __int__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

        def __str__(self):
            return f'{self._nome} | {self._categoria}'
        
        @classmethod
        def listar_restaurantes(cls):
            # Exibe a lista dde todos os restaurantes cadastrados
            print(" ")
            print(f"{'Nome do restaurante' .ljust(25)} | {'Avalição' .ljust(25)} | {'Status'}")
            for restaurante in cls.restaurantes:
                        print(f"{restaurante._nome.ljust(25)} | {restaurante.ativo} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}")

        @property
        def ativo(self):
        #Retorna um spimbolo visual representando se o restaurante está ativo ou inativo
            return '⌧' if self._ativo else '☐'   
        
        def alternar_estado(self):
             self._ativo = not self._ativo

        def receber_avaliacao(self, cliente, nota):
             #Adiciona uma nova avaliação ao restaurante, desde que seja de 0 a 10
             if 0 <= nota <= 10:
                  avaliacao = Avaliacao(cliente, nota)
                  self._avaliacao.append(avaliacao)
             else:
                print("A nota deve estar etre 0 e 10.")

        @property
        def media_avaliacoes(self):
             if not self._avaliacao:
                  return '-'
             soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
             quantidade_de_notas = len(self._avaliacao)
             media = round(soma_das_notas / quantidade_de_notas, 1)
             return media
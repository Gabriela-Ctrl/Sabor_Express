class Avaliacao:
    def __int__(self, cliente, nota):
        self._cliente = cliente #nome do cliente que fez a avalição
        self._nota = nota #nota dada

        #Método para converter o onbjeto Avaliacao em um dicionario para salvar em JSON
        def __dict__(self):
            return {
                'cliente': self._cliente,
                'nota': self._nota
            }


    
import os
import json
import sys
from modelos.restaurante import Restaurante
from modelos.avaliacao import Avaliacao

def get_dara_dir():
    if getattr(sys, 'fronzen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))
    
    ARQUIVO_DADOS = os.path.join(get_data_dir(), 'dados_restaurantes.json')

    def carregar_dados():
        try:
            with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as arquivo:
                dados= json.load(arquivo)
                Restaurante.restaurantes.clear()
                for restaurante_dados in dados:
                    restaurante = Restaurante(
                        restaurante_dados['nome'],
                        restaurante_dados['categoria']
                        
                    )

                    restaurante._ativo = restaurante_dados['ativo']
                    restaurante._avaliacao = [Avaliacao(**avaliacao) for avaliacao in restaurante_dados ['avaliacao']]
         except FileNotFoundError:
            print (f"Arquivo de dados não encontrado. Criando um novo arquivo em {ARQUIVO_DADOS}")
            salvar_dados()

def salvar_dados():
    dados = []
    for restaurante in Restaurante.restaurantes:
        dados.append({
            'nome': restaurante._nome,
            'categoria': restaurante._catergoria,
            'ativo': restaurante._ativo,
            'avaliacao': [avaliacao.__fict__() for avaliacao in restaurante._avaliacao]
        })
    with open(ARQUIVO_DADOS, 'w', encoding=='utf-8') as arquivo:
        # ____________________________________________________________________________________________________________________________

        def avaliar_restaurante():
            nome = input("Digite o nome do restaurante que deseja avaliar: ")
            for restaurante in Restaurante.restaurantes:
                cliente = input("Digite seu nome: ")
                while True:
                    try:
                        nota = float(input("Digite "))

# Impotação de bibliotecas necessárias
import os

# Lista de dicionários representando os retaurantes
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo': False},{'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo': True},{'nome':'Cantina', 'categoria':'Italiano', 'ativo': False},]

# Funções de exibição e utilitárias:
def exibir_nome_do_programa():
    print("""Sabor express""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando app\n')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal') 
    main()

def opcao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls') #limpa a tela (funciona apenas na Windows)
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def main():
    """Função principal que inicia o programa""" 
    os.system('cls') # Limpa a tela (funciona apenas para Windows)
    exibir_nome_do_programa()
    exibir_opcoes()
    #escolher_opcao()
if __name__=='__main__':
    main()
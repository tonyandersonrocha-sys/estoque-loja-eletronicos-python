# ==========================================================
# Sistema de Controle de Estoque para Loja de Eletrônicos
# Autor: Tony Anderson
# Descrição: Menu principal e controle do fluxo do sistema
# ==========================================================

# Importa o módulo OS para comandos do sistema (limpar tela)
import os

# Importa biblioteca para cores no terminal
from colorama import init, Fore, Style

# Importa funções do módulo estoque.py
from estoque import (
    carregar_estoque,
    salvar_estoque,
    listar_produtos,
    adicionar_produto,
    atualizar_produto,
    excluir_produto
)

# Inicializa o colorama (autoreset evita sujeira de cor no terminal)
init(autoreset=True)


# ----------------------------------------------------------
# Função responsável por limpar a tela
# Funciona tanto no Windows quanto no Mac/Linux
# ----------------------------------------------------------
def limpar_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# ----------------------------------------------------------
# Função que pausa o sistema até o usuário pressionar ENTER
# ----------------------------------------------------------
def pausar():
    input(Fore.YELLOW + "\nPressione ENTER para continuar...")




# ----------------------------------------------------------
# Função que exibe o menu principal do sistema
# ----------------------------------------------------------
def exibir_menu():
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + " SISTEMA DE CONTROLE DE ESTOQUE ")
    print(Fore.CYAN + "=" * 50)
    print(f"{Fore.GREEN}1 - Visualizar estoque")
    print(f"{Fore.GREEN}2 - Adicionar produto")
    print(f"{Fore.GREEN}3 - Atualizar produto")
    print(f"{Fore.GREEN}4 - Excluir produto")
    print(f"{Fore.GREEN}0 - Sair")
    print("=" * 50)


# ----------------------------------------------------------
# Função responsável por processar a opção escolhida
# ----------------------------------------------------------
def processar_opcao(opcao, estoque):
    if opcao == "1":
        listar_produtos(estoque)

    elif opcao == "2":
        adicionar_produto(estoque)
        salvar_estoque(estoque)

    elif opcao == "3":
        atualizar_produto(estoque)
        salvar_estoque(estoque)

    elif opcao == "4":
        excluir_produto(estoque)
        salvar_estoque(estoque)

    elif opcao == "0":
        print(Fore.GREEN + "Encerrando o sistema...")
        exit()

    else:
        print(Fore.RED + "Opção inválida!")


# ----------------------------------------------------------
# Função principal (equivalente ao MAIN)
# Controla todo o fluxo do sistema
# ----------------------------------------------------------
def executar_sistema():
    estoque = carregar_estoque()

    while True:
        limpar_tela()
        exibir_menu()
        opcao = input(f"{Fore.RED}Escolha uma opção: ").strip()
        limpar_tela()
        processar_opcao(opcao, estoque)
        pausar()


# ----------------------------------------------------------
# Ponto de entrada do programa
# ----------------------------------------------------------
executar_sistema()
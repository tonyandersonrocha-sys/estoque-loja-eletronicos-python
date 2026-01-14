# ==========================================================
# Módulo de manipulação do estoque
# Responsável por ler, salvar e manipular produtos
# ==========================================================

from colorama import Fore, Style


# ----------------------------------------------------------
# Carrega os produtos do arquivo estoque.txt
# ----------------------------------------------------------
def carregar_estoque():
    estoque = []

    try:
        with open("estoque.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome, preco, quantidade = linha.strip().split(";")
                estoque.append({
                    "nome": nome,
                    "preco": float(preco),
                    "quantidade": int(quantidade)
                })
    except FileNotFoundError:
        pass  # Caso o arquivo não exista, inicia estoque vazio

    return estoque


# ----------------------------------------------------------
# Salva o estoque no arquivo estoque.txt
# ----------------------------------------------------------
def salvar_estoque(estoque):
    with open("estoque.txt", "w", encoding="utf-8") as arquivo:
        for produto in estoque:
            arquivo.write(
                f"{produto['nome']};{produto['preco']};{produto['quantidade']}\n"
            )


# ----------------------------------------------------------
# Lista todos os produtos do estoque
# ----------------------------------------------------------
def listar_produtos(estoque):
    if not estoque:
        print(Fore.RED + "Estoque vazio!")
        return

    for produto in estoque:
        print(
        f"{Fore.BLUE}{produto['nome']}{Style.RESET_ALL} | "
        f"{Fore.BLUE}R$ {produto['preco']:.2f}{Style.RESET_ALL} | "
        f"{Fore.BLUE}Qtd: {produto['quantidade']}{Style.RESET_ALL}"
)

# ----------------------------------------------------------
# Adiciona um novo produto ao estoque
# ----------------------------------------------------------
def adicionar_produto(estoque):
    nome = input("Nome do produto: ").strip()
    preco = float(input("Preço do produto: "))
    quantidade = int(input("Quantidade: "))

    estoque.append({
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    })

    print(Fore.GREEN + "Produto adicionado com sucesso!")


# ----------------------------------------------------------
# Atualiza um produto existente
# ----------------------------------------------------------
def atualizar_produto(estoque):
    nome = input("Nome do produto para atualizar: ").strip()

    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            produto["preco"] = float(input("Novo preço: "))
            produto["quantidade"] = int(input("Nova quantidade: "))
            print(Fore.GREEN + "Produto atualizado!")
            return

    print(Fore.RED + "Produto não encontrado!")


# ----------------------------------------------------------
# Exclui um produto do estoque
# ----------------------------------------------------------
def excluir_produto(estoque):
    nome = input("Nome do produto para excluir: ").strip()

    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            estoque.remove(produto)
            print(Fore.GREEN + "Produto excluído!")
            return

    print(Fore.RED + "Produto não encontrado!")
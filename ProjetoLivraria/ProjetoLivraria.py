livros = []
DESCONTO_PADRAO = 0.15

def cadastrar_livro():
    TITULO = input("Titulo: ")
    AUTOR = input("Autor: ")


    try:
        PRECO = float(input("Preço: "))
        if not isinstance(PRECO, float):
            raise ValueError
        
    except ValueError:
        print("Valor inválido")
        return

    try:
        estoque = int(input("Estoque: "))
        if not isinstance(estoque, int):
            raise ValueError
        
    except ValueError:
        print("Valor inválido")
        return

    livro = {
        "titulo": TITULO,
        "autor": AUTOR,
        "preco": PRECO,
        "estoque": estoque
    }

    livros.append(livro)


def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado")
        return
    
    for i, livro in enumerate(livros):
        print(f"Titulo: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Preço: {livro['preco']:.2f}")
        print(f"Estoque: {livro['estoque']}")

def venda():
    if not livros:
        print("Nenhum livro cadastrado")
        return
    
    try:
        indice = int(input("Indice do livro: "))
        if not isinstance(indice, int):
            raise ValueError
    except ValueError:
        print("Erro")
        return

    livro = livros[indice]

    try:
        quantidade = int(input("Insira quantidade: "))
        if not isinstance(quantidade, int):
            raise ValueError
        if quantidade <= 0:
            print("Quantidade invalida")
            return
        elif quantidade > livro["estoque"]:
            print("estoque insuficiente")
            return
    except ValueError:
        print("Erro")
        return

    valor_completo = livro["preco"] * quantidade
    desconto = 0

    if valor_completo > 100:
        desconto = valor_completo * DESCONTO_PADRAO
    
    valor_final = valor_completo - desconto

    livro["estoque"] = livro["estoque"] - quantidade

    print(f"Título: {livro['titulo']}")
    print(f"Quantidade: {quantidade}")
    print(f"Valor completo: R$ {valor_completo:.2f}")
    if desconto > 0:
        print(f"Desconto ({DESCONTO_PADRAO}%): R$ {desconto:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")
    print(f"Estoque: {livro['estoque']}\n")

#---------------------------------------------------

while True:
    
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Realizar venda")
    print("Qualquer outro valor para sair")
    
    menu = input("Opção: ")

    if menu == "1":
        cadastrar_livro()
    elif menu == "2":
        listar_livros()
    elif menu == "3":
        venda()
    else:
        break

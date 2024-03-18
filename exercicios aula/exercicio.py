carrinho = [] # Armazena os produtos comprados 
produtos = [
    {"id": 1, "descricao": "Celular", "preco": 1999.23}
    ,{"id": 109, "descricao": "Computador", "preco": 3999.23}
    ,{"id": 11, "descricao": "Roteador", "preco": 199.23}
]
cliente ={}

print("Escolha um produto")
for i in range(len(produtos)):
    print(produtos[i])
class Conta:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

class Despesa:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor


def criar_conta(nome, saldo):
    conta = Conta(nome, saldo)
    contas.append(conta)
    return conta

def ler_conta(nome):
    for conta in contas:
        if conta.nome == nome:
            return conta
    return None

def atualizar_conta(nome, novo_saldo):
    conta = ler_conta(nome)
    if conta:
        conta.saldo = novo_saldo
        return True
    return False

def deletar_conta(nome):
    conta = ler_conta(nome)
    if conta:
        contas.remove(conta)
        return True
    return False

def criar_despesa(descricao, valor):
    despesa = Despesa(descricao, valor)
    despesas.append(despesa)
    return despesa

def ler_despesas():
    return despesas

def atualizar_despesa(descricao, novo_valor):
    for despesa in despesas:
        if despesa.descricao == descricao:
            despesa.valor = novo_valor
            return True
    return False

def deletar_despesa(descricao):
    for despesa in despesas:
        if despesa.descricao == descricao:
            despesas.remove(despesa)
            return True
    return False

# Exemplo de uso:
conta1 = criar_conta("Conta A", 1000)
conta2 = criar_conta("Conta B", 2000)

print("Contas:")
for conta in contas:
    print(f"Nome: {conta.nome}, Saldo: {conta.saldo}")

despesa1 = criar_despesa("Compras", 500)
despesa2 = criar_despesa("Aluguel", 1000)

print("\nDespesas:")
for despesa in despesas:
    print(f"Descrição: {despesa.descricao}, Valor: {despesa.valor}")

atualizar_conta("Conta A", 1500)

print("\nContas após atualização:")
for conta in contas:
    print(f"Nome: {conta.nome}, Saldo: {conta.saldo}")

deletar_despesa("Aluguel")

print("\nDespesas após deleção:")
for despesa in despesas:
    print(f"Descrição: {despesa.descricao}, Valor: {despesa.valor}")
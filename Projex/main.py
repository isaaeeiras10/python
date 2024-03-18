from lib.funcoes import atualizar_conta, atualizar_despesa, deletar_conta, deletar_despesa
from dados import contas, despesas

def main():
    
    while True:
        print('''
        [ 1 ] Criar contas e despesas 
        [ 2 ] Ler contas e despesas 
        [ 3 ] Atualizar contas e despesas
        [ 4 ] Excluir contas e despesas
        [ 5 ] Sair 
    ''')
         # Exibir contas e despesas antes das atualizações
        print("Contas antes da atualização:")
        for conta in contas:
            print(f"Nome: {conta.nome}, Saldo: {conta.saldo}")

        print("\nDespesas antes da atualização:")
        for despesa in despesas:
            print(f"Descrição: {despesa.descricao}, Valor: {despesa.valor}")

        # Atualizar uma conta e uma despesa
        atualizar_conta(contas,"Conta A", 1500)
        atualizar_despesa("Compras", 600)

        # Excluir uma conta e uma despesa
        deletar_conta("Conta B")
        deletar_despesa("Aluguel")

        # Exibir contas e despesas após as atualizações e exclusões
        print("\nContas após as atualizações e exclusões:")
        for conta in contas:
            print(f"Nome: {conta.nome}, Saldo: {conta.saldo}")

        print("\nDespesas após as atualizações e exclusões:")
        for despesa in despesa:
            print(f"Descrição: {despesa.descricao}, Valor: {despesa.valor}")

if __name__ == "__main__":
    main()
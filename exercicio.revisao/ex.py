numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O primeiro número é maior:", numero1)
elif numero2 > numero1:
    print("O segundo número é maior:", numero2)
else:
    print("Os números são iguais:", numero1)

# 2) Dado a venda de um produto calcule a comissão
# conforme a tabela abaixo.
# Se venda › 100000 (cem mil) comissão 5% # senão se venda › 50000 (cinquenta mil) comissão 7%
# senão comissão 10%
    
venda: float = float(input("Valor venda: "))
def calcular_comissao(valor_venda):
    if valor_venda > 100000:
        comissao = valor_venda * 0.05
    elif valor_venda > 50000:
        comissao = valor_venda * 0.07
    else:
        comissao = valor_venda * 0.10
    return comissao

# Exemplo de uso:
venda = float(input("Digite o valor da venda: "))
comissao = calcular_comissao(venda)
print("A comissão é:", comissao)
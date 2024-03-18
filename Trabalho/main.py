import random_data
import funcoes

def main():
    data = random_data.data

    while True:
        print("\nEscolha uma opção:")
        print("1. Quantidade de pessoas maiores de 50 anos")
        print("2. Quantidade de pessoas que ganham mais de R$ 2000 e a porcentagem")
        print("3. Nome, salário, idade e profissão das 3 pessoas com maiores salários")
        print("4. Média salarial de cada profissão")
        print("5. Intervalo da maioria das idades e o sexo de quem ganha mais de R$ 2000")
        print("0. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            print("Quantidade de pessoas maiores de 50 anos:", funcoes.maiores(data))
        elif opcao == "2":
            salario, porcentagem = funcoes.salario(data)
            print("Quantidade de pessoas que ganham mais de R$ 2000:", salario)
            print("Porcentagem:", porcentagem, "%")
        elif opcao == "3":
            print("Top 3 salários:")
            for pessoa in funcoes.maxsalarios(data):
                print("Nome:", pessoa['nome'], "- Salário:", pessoa['salario'], "- Idade:", pessoa['idade'], "- Profissão:", pessoa['profissao'])
        elif opcao == "4":
            print("Média salarial de cada profissão:")
            media_salarial = funcoes.media_profissao(data)
            for profissao, media in media_salarial.items():
                print(profissao + ":", media)
        elif opcao == "5":
            intervalo_idades, sexo_maior_2000 = funcoes.intervalo_idades_sexo_maior_2000(data)
            print("Intervalo da maioria das idades:", intervalo_idades)
            print("Sexo de quem ganha mais de R$ 2000:", sexo_maior_2000)
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

if __name__ == "_main_":
    main()
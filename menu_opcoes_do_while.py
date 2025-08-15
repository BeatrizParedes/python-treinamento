"Crie um programa que exiba um menu de opções e permita ao usuário escolher uma ação"
"Como somar dois números, subtrair, multiplicar etc."
"O menu deve continuar sendo exibido até o usuário escolher a opção de sair."

def menu():
    while True:
        print("Menu de Opções:")
        print("1. Somar dois números")
        print("2. Subtrair dois números")
        print("3. Multiplicar dois números")
        print("4. Dividir dois números")
        print("5. Sair")

        opcao =input("Escolha uma opção (1-5) (5 para sair): ")
        if opcao == '1':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(f"A soma é: {num1 + num2}")
        elif opcao == '2':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(f"A subtração é: {num1 - num2}")
        elif opcao == '3':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(f"A multiplicação é: {num1 * num2}")
        elif opcao == '4':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if num2 != 0:
                print(f"A divisão é: {num1 / num2}")
            else:
                print("Erro: Divisão por zero.")
        elif opcao == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
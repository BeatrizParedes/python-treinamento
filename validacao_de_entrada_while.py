"Crie um programa que leia um número inteiro entre 1 e 10. Caso o valor seja inválido, continue pedindo a entrada até que um número válido seja fornecido"

def validacao_de_entrada():
    numero=int(input("Digite um número entre 1 e 10: "))
    
    while numero<1 or numero>10:
        print("Número inválido. Tente novamente. ")
        numero=int(input("Digite um número entre 1 e 10: "))

    print(f"Número válido: {numero}")

if __name__=="__main__":
    validacao_de_entrada()
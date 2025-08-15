"Desenvolva um programa que leia números inteiros do usuário e exiba a soma acumulada. O programa deve terminar quando o usuário digitar o número zero."

def soma_acumulada():
    num1=0
    soma=0
    num1=int(input("Digite um número inteiro (0 para sair): "))
    while num1 !=0:
        soma += num1
        num1=int(input("Digite outro número inteiro (0 para sair): "))
        
    print(f"Soma acumulada: {soma}")

if __name__ == "__main__":
    soma_acumulada()
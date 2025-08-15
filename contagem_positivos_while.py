"Escreva um programa que leia números inteiros e exiba quantos desses números são positivos. O programa deve parar quando o usuário digitar um número negativo."

def contagem_positivos():
    contagem_positivos=0
    numero=int(input("Digite um número (negativo para sair): "))
    while numero>=0:
        contagem_positivos +=1
        numero=int(input("Digite outro número (negativo para sair):"))
    print(f"Quantidade de números positivos: {contagem_positivos}")

if __name__ == "__main__":
    contagem_positivos()
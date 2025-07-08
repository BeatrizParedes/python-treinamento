"Escreva um programa que exiba todos os números ímpares entre 1 e 50"

def impares():
    for i in range(1, 51, 2): #No exercício de pares começa no 2 e nesse começa em 1 para dar certo
        print(i)

if __name__=="__main__":
    impares()
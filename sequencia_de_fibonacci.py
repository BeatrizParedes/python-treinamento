"Escreva um programa que exiba os primeiros 10 termos da sequência de Fibonacci."

def sequencia_fibonacci():
    termo1 =int(input("Escolha um número para iniciar a sequência de Fibonacci: "))
    termo2 = int(input("Escolha outro número para continuar a sequência: "))
    print(f"{termo1}, {termo2}", end=", ")

    for i in range(3, 11):
        termo3=termo1+termo2
        print(termo3, end=" ")
        termo1, termo2=termo2, termo3

if __name__ == "__main__":
    sequencia_fibonacci()
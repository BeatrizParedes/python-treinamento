"Desenvolva um programa que conte quantos números múltiplos de 3 existem no intervalo de 1 a 100."

def contagem_multiplos():
    contador = 0

    for i in range(1, 101):
        if i % 3 == 0:
            contador += 1

    print(f"Existem {contador} números múltiplos de 3 no intervalo de 1 a 100.")

if __name__ == "__main__":
    contagem_multiplos()

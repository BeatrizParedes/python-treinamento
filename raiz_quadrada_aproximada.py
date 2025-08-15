"crie um programa que leia um número intiero positivo e encontre a raiz quadrada aproximada desse número. "
"Continue a tentativa até encontrar a aproximação correta."

def raiz_quadrada_aproximada():
    num = int(input("Digite um número inteiro positivo: "))
    raiz_aprox = 0
    
    while raiz_aprox * raiz_aprox <= num:
        raiz_aprox += 1

    # Volta 1, pois passou do valor correto
    raiz_aprox -= 1

    if raiz_aprox * raiz_aprox == num:
        print(f"Raiz quadrada exata de {num} é {raiz_aprox}")
    else:
        print(f"Raiz quadrada aproximada de {num} é {raiz_aprox}")

if __name__ == "__main__":
    raiz_quadrada_aproximada()

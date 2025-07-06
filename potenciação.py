"Escreva um programa que leia dois número inteiros do usuário e exiba o resultado da potenciação do primeiro número elevado ao segundo número"
"Use o método Math.pow"
"Dica: pow recebe dois argumentos, o primeiro a base e o segundo o expoente"

def potenciacao():
    base = int(input("Escreva a base: "))
    expoente = int(input("Escreva o expoente: "))
    resultado = pow(base,expoente)

    print(f"O resultado da potenciação de {base} elevado a {expoente} é: {resultado}")
    
if __name__=="__main__":
    potenciacao()
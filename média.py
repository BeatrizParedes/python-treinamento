"Escreca um programa que leia três números inteiros do usuário e calcule a média aritmética deles."
"Exiba o resultado no console"
"Dica: Sempre que os exercícios pedirem para 'ler' algo, você deve utilizar a classe Scanner."

def media():
    num1 = int(input("Escreva o primeiro número: "))
    num2 = int(input("Escreva o segundo número: "))
    num3 = int(input("Escreva o terceiro numero: "))
    media_notas= (num1+num3+num2)/3

    print(f"A média de {num1,num2,num3} é: ",media_notas)

if __name__ == "__main__":
    media()
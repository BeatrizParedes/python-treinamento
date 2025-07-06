"Crie um programa que leia três numeros inteiros "
"Verifique se pelo menos um deles é maior que 10 (usando o operador ||)"
"Em seguida, verifique se todos são maiores que 10 (usando o operador &&)"

def operadores():
    num1=int(input("Escolha o primeiro número "))
    num2=int(input("Escolha o segundo número: "))
    num3=int(input("Escolha o terceiro número "))

    if(num1>10 or num2>10 or num3 >10):
        print("Pelo menos um dos números que você escolheu é maior que 10")
    else:
        print("Nenhum dos números é maior que 10")

    if(num1 >10 and num2>10 and num3 >10):
        print("Todos os número que você escolheu são maiores que 10 ")
    else:
        print("Nem todos os números são maiores que 10")


if __name__=="__main__":
    operadores()
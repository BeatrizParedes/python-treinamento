"Escreva um programa que leia um número de 1 a 4 e exiba o nome da estação do ano correspondente"
"1 - Verão"
"2 - Outono"
"3 - Inverno"
"4 - Primavera"

def estacao():
    escolha=int(input("Escolha um número para representar uma estação\n1- Verão\n2- Outono\n3- Inverno\n4- Primavera"))
    if (escolha==1):
        print("Sua escolha foi o verão")
    elif (escolha==2):
        print("Sua escolha foi outono")
    elif (escolha==3):
        print("Sua escolha foi Inverno")
    elif (escolha==4):
        print("Sua escolha foi a primavera")
    else:
        print("Faça uma escolha dentro do intervalo")
if __name__=="__main__":
    estacao()
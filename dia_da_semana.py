"Escreva um programa que leia um número inteiro de 1 a 7 e exiba o nome do dia da semana correspondente"
"(1 para domingo, 2 para segunda-feira, etc)"

def dias():
    dia=int(input("Escreva um número para escolher um dia da semana (1-7)\n1 - Domingo\n2 - Segunda\n3 - Terça\n4 - Quarta\n5 - Quinta\n6 - Sexta\n7 - Sábado "))

    if (dia==1):
        print("O dia escolhido foi o Domingo")
    elif (dia==2):
        print("O dia escolhido foi a Segunda")
    elif (dia == 3):
        print("O dia da semana foi a Terça")
    elif (dia==4):
        print("O dia da semana foi a Quarta")
    elif (dia==5):
        print("O dia da semana foi a Quinta")
    elif (dia==6):
        print("O dia da semana foi a Sexta")
    elif (dia==7):
        print("O dia da semana doi o Sábado")
    else:
        print("Você não escolheu um número válido")

if __name__=="__main__":
    dias()
"Crie um programa que leia a idade de uma pessoa e a classifique em uma das seguintes categorias"
"0 a 12: Criança"
"13 a 17: Adolescente"
"18 a 59: Adulto"
"60 ou mais: idoso"
"Utilize a estrutura if-elif-else para definir as condições de classificação"

def idade():
    escolha=int(input("Qual a idade que você quer classificar? "))

    if (0<=escolha<=12):
        print("A idade é de uma criança")
    elif (13<=escolha<=17):
        print("A idade é de um adolescente")
    elif (18<=escolha<=59):
        print("A idade é de um adulto")
    elif (60<=escolha):
        print("A idade é de um idoso")
    else:
        print("Por favor insira uma idade válida")

if __name__=="__main__":
    idade()
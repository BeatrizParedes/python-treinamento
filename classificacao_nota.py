"Crie um programa que leia uma nota e 0 a 10 e classifique a nota de acordo com as seguintes categorias:"
"10 - Excelente"
"8 e 9 - Muito bom"
"6 e 7 - Bom"
"5 - Regular"
"0 a 4 - Insuficiente"

def notas():
    nota=int(input("Escreva sua nota: "))

    if (nota==10):
        print("Excelente")
    elif (nota==8 or nota==9):
        print("Muito bom")
    elif (nota==6 or nota==7):
        print("Bom")
    elif (nota==5):
        print("Regular")
    elif (0<=nota<=4):
        print("Insuficiente")
    else:
        print("Insira um valor válido")

if __name__=="__main__":
    notas()
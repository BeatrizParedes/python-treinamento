"Crie um programa que declare e inicialize variáveis de todos os tipos primitivos em Python "
"(int, float, str, bool) "
"Exiba o valor de cada variável no console"

def notas():
    qtd = int  (2)
    nome = str (input("Insira seu nome: "))
    nota1 = float (input("Insira nota 1: "))
    nota2 = float (input("Insira nota 2: "))
    media = ((nota1+nota2)/qtd)
    
    print(nome)
    print(media)

    if (media>=7):
        aprovado = True
        print ("Você foi aprovado!")
    elif (media<7):
        print ("Você foi reprovado!")
        aprovado = False
    else:
        print ("Houve algum erro no sistema")

    print(aprovado)

if __name__ == "__main__":
    notas()


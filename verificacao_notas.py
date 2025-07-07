"Crie um programa que leia uma nota de 0 a 100 e exiba uma mensagem de aprovação se a nota for maior ou igual a 60."
"Caso contrário, exiba uma mensagem de reprovação"

def notas():
    nota = int(input("Digite uma nota (0 a 100): "))

    if nota>=60:
        print("Você está aprovado")
    else:
        print("Você está reprovado")
        
if __name__=="__main__":
    notas()
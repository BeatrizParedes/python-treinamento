"Crie um programa que leia a idade de uma pessoa e verifque se ela é elegível para votar"
"Idade igual ou superior a 18 anos"

def maioridade():
    idade = int(input("Qual idade você deseja verificar? "))
    if (idade>=18):
        print("A idade é elegível para votar")
    else:
        print("A idade não é elegível para votar")

if __name__=="__main__":
    maioridade()
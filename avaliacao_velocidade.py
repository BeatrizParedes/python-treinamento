"Crie um programa que leia a velocidade de um veículo"
"Exiba uma mensagem dizendo se o veículo está dentro do limite de velocidade (até 60km/h)"
"Acima do limite (entre 61km/h e 80km/h)"
"Muito acima do limite (acima de 80km/h)"

def velocidade():
    velocidade=int(input("Escreva a velocidade do veículo: "))
    if (velocidade<=60):
        print("O veículo está dentro do limite de velocidade")
    elif (velocidade<=80):
        print("O veículo está acima do limite")
    else:
        print("O veículo está muito acima do limite")
if __name__=="__main__":
    velocidade()
"Escreva um programa que leia a temperatura atual em graus Celsius e exiba uma mensagem dizendo se o clima está:"
"Frio (abaixo de 15ºC)"
"Agradável (entre 15ºC e 30ºC)"
"Quente (acima de 30º)"

def clima():
    temperatura=int(input("Escreva a temperatura de hoje: "))

    if (temperatura<=15):
        print("A temperatura está fria")
    elif (15<temperatura<=30):
        print("A temperatura está agradável")
    else:
        print("A temperatura está quente")

if __name__=="__main__":
    clima()
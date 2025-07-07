"Desenvolva um programa que leia o valor de uma compra e aplique um desconto de 10% se o valor for superior a R$100,00."
"Exiba o valor final com ou sem desconto"

def desconto():
    print("Olá, seja bem-vindo")
    valordacompra=float(int(input("Qual o valor da compra ")))
    if (valordacompra>100):
        valordacompra*=0.90 #Aplicando o desconto de 10%

        print(f"Desconto aplicado! Valor final R$ {valordacompra:.2f}")

    else:
        print(f"Sem desconto. Valor final: R$ {valordacompra:.2f}")

if __name__=="__main__":
    desconto()
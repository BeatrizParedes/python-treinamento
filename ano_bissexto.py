"Crie um programa que leia um ano e verifique se ele é bissexto"
"Um ano é bissexto se for divisível por 4, mas não por 100, exceto se for divisível por 400"

def bissexto():
    ano=int(input("Escreva o ano que você deseja analisar: "))
    if (ano%4==0 and ano%100!=0 or ano%400==0):
        print("O ano é bissexto")
    else:
        print("O ano não é bissexto")

if __name__=="__main__":
    bissexto()
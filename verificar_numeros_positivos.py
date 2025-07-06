"Escreva um programa que leia três números inteiros e verifique se pelo menos dois deles são positivos"

def positivos():
    num1=int(input("Escreva o primeiro número: "))
    num2=int(input("Escreva o segundo número: "))
    num3=int(input("Escreva o terceiro número: "))
    contador=0

    if(num1>0):
        contador+=1
    if(num2>0):
        contador+=1
    if(num3>0):
        contador+=1
    
    if(contador>=2):
        print("Pelo menos dois desses números são positivos")

if __name__ =="__main__":
    positivos()
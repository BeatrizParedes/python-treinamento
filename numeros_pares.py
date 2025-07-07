"Desenvolva um programa que exiba todos os números pares de 1 a 20"

def pares():
    for i in range (1,21):
        if (i%2==0):
            print(i)

if __name__=="__main__":
    pares()
    
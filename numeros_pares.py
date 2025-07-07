"Desenvolva um programa que exiba todos os números pares de 1 a 20"

def pares():
    for i in range (1,21):
        if (i%2==0):
            print(i)

if __name__=="__main__":
    pares()
    
"""

Outra forma de fazer

for i in range (2,21,2): 
    print(i)

O primeiro argumento 2 é o valor inicial
O segundo artumento 21 indica que o laço vai aé 20 (o limite superior não é incluído)
O terceiro argumento 2 é o passo da contagem, farantindo que apenas números pares sejam exibidos
    
"""
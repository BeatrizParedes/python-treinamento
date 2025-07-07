"Crie um programa que exiba os números de 10 a 1, em ordem decrescene, usando um laço for"

def decrescente():
    for i in range (10, 0, -1): #O primeiro argumento (10) é o valor inicial
                                #O segundo argumento (0) indica que o laço vai a´te 1, pois o limite superior não é incluído
                                #O terceiro argumento (-1) indica que a contagem é decrescente, decrementando 1 a cada iteração
        print(i)
if __name__=="__main__":
    decrescente()
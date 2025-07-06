"Crie um programa que declare uma variável inteira, atribua um valor a ela"
"Em seguida, modifique o valor utilizando os operadores de atribuição (+=, -=, *=, /=, %=)"

def atribuicao():
    valor=10

    valor+=5
    print("Após valor +=5:", valor)
    valor=10 #Deixei a variável com valor inicial para testar os próximos passos

    valor*=2
    print("Após valor *=2:", valor)
    valor=10

    valor/=4
    print("Após valor/=4:", valor)
    valor=10

    valor%=3
    print("Após valor %=3:", valor)

if __name__=="__main__":
    atribuicao()
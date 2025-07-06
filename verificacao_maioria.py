"Escreva um programa ue leia a idade de três pessoas e verifique se pelo menos duas delas são maiores de idade (18 anos ou mais)"

def maioria():
    idade1=int(input("Escreva a primeira idade "))
    idade2=int(input("Escreva a segunda idade "))
    idade3=int(input("Escreva a terceira idade "))
    maioridade=0

    if (idade1>=18):
        maioridade+=1
    if (idade2>=18):
        maioridade+=1
    if (idade3>=18):
        maioridade+=1
    
    if (maioridade>=2):
        print("Pelo menos 2 das idades que você me forneceu são maiores de 18 anos")
    else:
        print("Há 1 pessoa ou menos que atingiu a maioridade nas que você me forneceu")

if __name__=="__main__":
    maioria()
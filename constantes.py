"Crie um programa que utilize a palavra-chave para declarar uma constante que representa a velocidade no vácuo"
"Tente alterar o valor da constante e observe o comportamento do Python"

def constante():
    velocidade_no_vacuo=299792458 #Velocidade em metros por segundo
    print(f"Essa é a velocidade da luz no vácuo: {velocidade_no_vacuo} m/s")

    #Redeclarando a constante
    try:
        velocidade_no_vacuo=3000000000 #Deveria gerar erro na execução mas acho que o python deixou passar
        print(velocidade_no_vacuo)

    except Exception as velocidade_no_vacuo:
            print(f"Erro ao tentar alterar a constante: {velocidade_no_vacuo}")

if __name__=="__main__":
    constante()
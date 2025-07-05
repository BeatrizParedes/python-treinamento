"Escreva um programa que declare variáveis locais e globais (dentro de uma classe)"
"Inicialize e exib o valor de ambas as variáveis no console"

class tiposDeVariavel:
    variavel_global = 10 #Essa variável pode ser acessada por qualquer método da classe

    def tipos_de_variavel(self):
        variavel_local = 5 #Variável Local é declarada dentro do método tipos_de_variavel, sendo local a esse método, ou seja, só podendo ser acessada dentro dele

        print(f"Valor da variável global: {self.variavel_global}")
        print(f"Valor da variável local: {variavel_local}")

if __name__== "__main__":
    variaveis = tiposDeVariavel()
    variaveis.tipos_de_variavel()

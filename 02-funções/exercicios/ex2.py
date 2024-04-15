#Ex02 - Tabuada de Um Número: Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.

print("\nTabuada!")

numero = int(input("Digite um número\n"))

print("\nAgora irei te mostrar a tabuada do numero", numero)

def calculartabuada(numero):
    i = 1
    while (i <= 10): 
        produto = numero * i 
        print(numero, "*", i, "=", produto) 
        i = i + 1

calculartabuada(numero)
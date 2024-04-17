'''
 Verificador de Palíndromos: Solicite ao usuário que digite uma palavra ou frase e verifique se é um palíndromo
 (ou seja, pode ser lida de frente para trás e de trás para frente da mesma forma).
'''

def verificacao (entrada):
    if entrada == entrada[::-1]:
        print("O que você digitou é um palíndromo!")
    else: 
        print("Não é palíndromo")


entrada = str(input("Digite uma palavra ou frase!\n"))

verificacao(entrada)
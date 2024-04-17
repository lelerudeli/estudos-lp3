'''
Função de Contagem de Palavras: Escreva uma função que receba uma string (frase) como argumento e retorne um dicionário
onde as chaves são as palavras únicas no texto e os valores são o número de vezes que cada palavra aparece no texto. 
Depois, teste a função com diferentes textos fornecidos pelo usuário.
'''

def contagem (frase):
    
    palavras = frase.split()
    dic = {}

    for palavra in palavras:
        dic.update({palavra: palavras.count(palavra)})

    return dic 

frase = str(input("Digite uma frase: "))

print("\nCerto! Agora vamos contar quantas vezes cada palavra foi usada nesta frase.")

print(contagem(frase))


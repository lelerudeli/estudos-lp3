# identificadores
# letras, numero e _ 
# case sensitive     
idade = 20
Idade = 20 
# palavras reservadas: if, for, class, when 


# variavel 
# java:  float velocidade = 20.2f;
# python: 
nome = "lelezinha"
velocidade = 20.2 
velocidade = velocidade + 10 


# constante 
# nao existe constante 
# convenção - identificador de uma constante com as letras maiúsculas
PI = 3.14
# valor pode ser alterado 
PI = 99.9

# comentário de uma linha 

'''
comentario 
de 
várias
linhas 
'''

# docstring 
# documentar códigode funções, classes, etc 

def somar (nmr1, nmr2): 
    
    '''
    função que soma dois numeros 
    
    :parametro nmr1: primeiro numero 
    :parametro nmr2: segundo numero 
    :return: soma dos numeros 
    '''

    return nmr1 + nmr2

somar (2,3)

# posso colocar QUALQUER valor em nmr1, pois python não tem tipo definido 
# ex
somar ("lele", True)
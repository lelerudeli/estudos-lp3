# tipos de dados 
# int, float, complex

# int 
idade = 20
temp = 25

# float
velocidade = 55.5
altura = 153.4

# boolean  
verdade = True 
mentira = False 

# Strings 
# sequencia de caracteres 
nome = "lelet rudeli"
nome = "isinha pantolfo"

# multilinha
# manter a formatação da string 
frase = """
oierrrr, 
bla bla bla 
"""

# intepolação de string 
# f-strings 
nome = "lele"
idade = 17 
frase = f"Ola {nome}!! Você tem {idade} anos?"
print (frase)

# e o char? 
# o char é uma string de um caractere só 
letra = 'a'
letra = 'b'

'''aqui estamos colocando duas variáveis com o mesmo nome, 
se formos ler isso, a ultima definição é a levada em conta '''

# acesso a um caractere da string 
nome = "lelezinha"
print (nome[0])
print (nome[-1]) #lendo de tras pra frente 
print (nome[-3]) 


# string sao objetos --> sao métodos 

print(nome.capitalize) #pimeira letra em maiúsculo 
nome.upper()  # devolve o valor em maiúsculo 


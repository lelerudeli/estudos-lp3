#operadores aritméticos 
# + - / * % (resto da divisao) ** potencia 

nota1 = 10.0
nota2 = 8.0
nota3 = 5.5

media = (nota1+nota2+nota3) / 3 

# 10 ao quadrado
nmr = 10 

ao_quadrado = nmr*nmr 
ao_quadrado = nmr**2 

# Operadores lógicos 
# and, or, not 

print (True and True) # true
print (True and False) # false 
print (False and True) # false 
print (False and False) # false 

print (True or True) # true
print (True or False) # true 
print (False or True) # true
print (False or False) # false

verdade = True and False 

# permite entrada no sistema 
# usuario nao bloqueado E
# usuario é um funcionario E
# hora entre 8h e 18h (horario comercial)
# ---
# caso for adm pode acessar de qualquer forma 

u_bloqueado = False 
u_funcionario = True
hora = 23
u_adm = False 

func_ativo = u_funcionario and not u_bloqueado
h_comercial = hora >=8 and hora <=18 # false || 23 horas

if (func_ativo and h_comercial) or u_adm:
    print('acesso liberado')
else:
    print('acesso negado')

#Outro arquivo || usando funcao 
def dentro_h_comercial (hora):  #def= funcao
    return hora >=8 and hora <=18 


# Operadores de comparação 
# ==, !=, >, <, <=, >= 

n1 = 10.0
n2 = 5.5

#aluno foi melhor na primeira prova ou na segunda? 

if n1 > n2 :
    print('aluno foi melhor na prova 1!!')
else: 
    print('aluno foi melhor na prova 2!!  - ou teve a mesma nota nas duas - ')


# operador is is not 
# operador de identidade 
# comparar se os objetos sao os mesmos 
# mesmo espaco de memoria 

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) # compara se os valores são iguais , True 

print(a is b) # compara espaço de memória, False, pq sao variaveis diferentes, não ocupam o mesmo espaço de memória 

c = b 
print(c is b) # True 

# operador in, not in
# usado para verificar se um elemento existe em uma sequência 
# str, list, tupla

#opcoes = {
#    'sim': ['sim', 's', 'y', 'yes'],
#   'nao': ['nao', 'não', 'n']
#}

opcoes = ('sim', 'nao', 'talvez')
opcao = input('digite uma opcao ')
opcao = opcao.lower().strip() 
# lower -> deixa tudo em minuscula (bom para experiencia do usuario, se digitar  SIM, vai funcionar tb)
# strip -> remove os espaços, inicio e fim 

if opcao in opcoes:
    print('ok')
else:
    print('invalido')

# if 
idade = 20

# if condicao 
#       codigo 

if idade >= 18:
    print('maior de idade')
    print('parabéns')


# if else 
if idade >= 18: 
    print('maior de idade')
else:
    print('menor de idade')


# if/elif/else 
# crianca = 0 - 12
# adolescente = 13 a 17 
# adulto = 18 a 59 
# idoso = 60 + 

if idade <= 12:
    print('cria')
elif idade <= 17:
    print('adolescente')
elif idade <=59:
    print('adulto')
else:
    print('idoso')


# exemplo de if aninhado 
email = 'lele@gmail.com'
senha = '123'

if email == 'lele@gmail.com':
    if senha == '123':
        print('acesso permitido')
    else: 
        print('invalido')
else:
    print('invalido')


# exemplo codigo melhorado 
if email == 'lele@gmail.com' and senha == '123':
    print('acesso permitido')
else: 
    print('invalido')


# entrada numero 
# 0 -  domingo 
# 1 - segunda 
# 2 - terca
# etc

dia = 1

if dia == 1:
    print('domingo')
elif dia == 2:
    print('segunda')

# ... forma mais facil e melhorada
dias = {
    1: 'domingo',
    2: 'segunda',
    3: 'terca',
    4: 'quarta',
    5: 'quinta',
    6: 'sexta',
    7: 'sabado'
} 

if dia in dias:
    print(dias[dia])
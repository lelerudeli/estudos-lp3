'''  Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente. 
Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número. '''

import random 
nmr = random.randint(1,100)
acertou = False 

print("\njoguinho de adivinhação")
print("adivinhe qual foi o número escolhido!!\n\n")

def advinhação (chute): 
    if (chute > nmr):
        print("não foi dessa vez, dê um palpite mais baixo!\n")
        return False
    elif (chute < nmr):
        print("não foi dessa vez, dê um palpite mais alto!\n")
        return False
    else: 
        print("você acertou!!")
        return True

while acertou == False: 
    chute = int(input('digite um número de 1 a 100\n'))
    advinhação(chute)

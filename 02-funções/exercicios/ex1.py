'''  Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente. 
Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número. '''

import random 
nmr = random.randint(1,100) 

print("\njoguinho de adivinhação")
print("adivinhe qual foi o número escolhido!!\n")

def advinhação (nmr): 

    while True: 

        chute = int(input('\ndigite um número de 1 a 100\n'))

        if (chute > nmr):
            print("\nnão foi dessa vez, dê um palpite mais baixo!")
        
        elif (chute < nmr):
            print("\nnão foi dessa vez, dê um palpite mais alto!")
                  
        else: 
            print("\nvocê acertou!!!")
            break
        
advinhação(nmr)

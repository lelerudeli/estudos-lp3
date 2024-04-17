'''
Jogo da Forca: Implemente uma versão simples do jogo da forca. O programa começa com uma palavra oculta (o usuário não vê)
e o usuário tenta adivinhar a palavra, letra por letra. 
O usuário tem um número limitado de tentativas para adivinhar toda a palavra.
'''

import random

def escolhePalavra():

    palavras = ["helicóptero", "geladeira", "gato", "chiclete", "computador", "garrafa"]
    return random.choice(palavras)

def forca():

    palavra = escolhePalavra()
    tentativas= []
    chances = 5

    while True:

        print("\nJogo da Forca ")

        for letra in palavra:
            if letra in tentativas:
                print (letra, end=" ")
            else:
                print("_", end=" ")
        
        
        print(f"\n\nVocê tem {chances} chances")
        print(f"\nEssas letras já foram utilizadas: {tentativas}")
        tentativa = input("\nDê um palpite: ")
        tentativa.lower()
        tentativas.append(tentativa)
        

        if tentativa not in palavra:
            chances -= 1

        acertou = True

        for letra in palavra:
            if letra not in tentativas:
                acertou = False

        if chances == 0 or acertou:
            break

    if acertou:
        print(f"Parabens :D \nVocê acertou restando {chances} chances!!!")
        
    else:
        print(f"Acabaram suas chances, você perdeu :( \nA palavra era: {palavra}")
        
            
forca()
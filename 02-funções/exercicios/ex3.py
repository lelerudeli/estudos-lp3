#Ex03 - Contador de Vogais e Consoantes: Peça ao usuário para digitar uma frase e retorne o número de vogais e consoantes na frase.


def contadorVC (frase):

    vogais = ["a", "e", "i", "o", "u"]
    
    V = 0
    C = 0
    
    letras = [letra for letra in frase.strip()]

    for i in letras: 
        if i in vogais:
            V = V + 1
        else: 
            C= C + 1

    print("Vogais: ", V)
    print("Consoantes: ", C)

frase = input("\ndigite uma frase: ")
print("\ncerto, agora vamos contar quantas vogais e quantas consoantes tem nela!")

contadorVC(frase)



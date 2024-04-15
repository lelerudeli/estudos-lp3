'''
Ex04 - Simulador de Eleições: Crie um programa que simule uma votação com três candidatos.
O programa deve pedir ao usuário para votar várias vezes e, no final, 
mostrar o número de votos de cada candidato e quem foi o vencedor.
'''

    
candidatos = {
        1: "Lele",
        2: "Panpan",
        3: "Henryzitos"
    }   

print("ELEIÇÃO\n opções: \n", candidatos)

votos1 = 0
votos2 = 0 
votos3 = 0 

def contagem():

    global votos1, votos2, votos3

    i = 0 
    for i in range(5):
        escolha = int(input("\ndigite seu voto com o número que representa seu canditado.\n"))

        if (escolha == 1 or escolha == 2 or escolha == 3):
            i += 1
            match escolha:
                case 1: 
                    votos1 += 1
                case 2: 
                    votos2 += 1
                case 3:
                    votos3 += 1
        else: 
            print("\nopção inválida! \ntente novamente")
            contagem()
            break            

    return votos3, votos2, votos1


def analise(votos1, votos2, votos3):

    print("\nVotação encerrada!")
    
    if(votos1 > votos2 and votos1 > votos3):
        print("\na Lele ganhou!!!")

    elif(votos2 > votos3 and votos2 > votos1):
        print("\na Panpan ganhou!!!")

    else:
        print("\no Henryzitos ganhou!!!")


contagem()
analise(votos1, votos2, votos3) 
        


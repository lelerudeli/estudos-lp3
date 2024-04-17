'''
Conversor de Notas Escolares: Baseado em uma pontuação fornecida pelo usuário (0 a 100), 
converta para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.
'''

def conversao(nota: int) -> str:
    
    sistemaLetras = {

        range(0,20): "F",
        range(21,40): "D",
        range(41,60): "C",
        range(61,80): "B",
        range(81,100): "A"

    }

    for letra in sistemaLetras.keys():
        if nota in letra: 
            print("Nota em número: ", nota)
            print("Nota convertida: ", sistemaLetras[letra])
        
            while (nota>100 or nota<0):
                return "Nota inválida"   
        

nota = int(input("Qual foi a sua nota? \n"))

print("\nCerto, agora vamos converter para o sistema de letras") 

conversao(nota)

    

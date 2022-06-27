'''Projeto 1 - Python'''

#Advinhe o número Python (Computador)

import random as rd

def Joga_Dado(): # Função para jogar o dado
    dado = rd.randint(1,100)
    return dado

def Adivinhar_Número(dado):   #Função para adivinhar o número
    a = int(input('Tente adivinhar o número do dado de 1 a 100: '))
    if a == dado:
        print('\nParabéns! Você acertou\n')
    else:
        print('Voce errou! Tente denovo.')
        Adivinhar_Número(dado)
    

def Chama_Menu():
    print(f'''Esse é meu primeiro projeto em Python. Bem-vindo :)

Para iniciar o jogo digite 1.
Para sair do jogo digite 2.''')
    decisao = int(input())   #INPUT DO PRINT ACIMA
    if decisao == 1:
        pass    #prosseguir para o código
    elif decisao == 2:
        exit(print('Obrigado! =)'))
    else:
        print('Não entendi')   #CHAMAR NOVAMENTE O MENU
        Chama_Menu()


#LOOP DE MENU DO CÓDIGO
while True:
    Chama_Menu()
    dado = Joga_Dado()
    Adivinhar_Número(dado)
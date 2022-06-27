##Encurtador de URL

import random as rd

####### MENU ######

def Menu():
    menu = int(input('''Digite 1 para criar um link curto.
Digite 2 para acessar o link original a partir de um link encurtado.
Digite 3 para encerrar o programa.
'''))
    if menu == 1:
        Gerador_De_Link()
    elif menu == 2:
        a = input('Digite aqui o link encurtado: ')
        print(f'Seu link é: {banco_de_dados.get(a)}')
    elif menu == 3:
        exit(print('Obrigado!'))
    else:
        print('Não entendi\n')
        Menu()

####### INICIO DO PROGRAMA ######

banco_de_dados = {}
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def Pede_Link():        #Pede o link a ser salvo e retorna o link
    link = str(input("Digite aqui a URL a ser encurtada: "))
    return link


def Encurta_Link():     #gera uma sequencia aleatória de números e letras retornando o final da url. Ex: www.xxxx.com/URL_ENCURTADA
    link = []
    for x in range(4):
        pt1 = str(rd.randint(1,9))
        pt2 = rd.sample(alfabeto,1)
        link.append(pt1)        #adiciona um número na lsta link
        link.extend(pt2)        #adiciona e concatena uma palavra na lista link
    link_encurtado = "".join(link)  #transforma lista numa string
    return link_encurtado   #retorna o final da URL encurtada
    

    
def Gerador_De_Link():      #Gera o link final e adiciona ao banco de dados em forma de dicionário.
    link = Pede_Link()
    short_url = Encurta_Link()
    short_url = "https://www.encurtadorurl/"+short_url
    banco_de_dados.update({short_url : link})
    print (f'Seu link encurtado é: {short_url}')



while True:
    Menu()
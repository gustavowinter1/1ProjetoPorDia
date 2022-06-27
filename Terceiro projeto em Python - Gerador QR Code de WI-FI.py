##Terceiro projeto em Python 
#Gerador de QR para Wi-Fi

#Gerador simples onde toda rede deve ser visível e WEP ou WPA, e possuir também uma senha.

#Gustavo_Winter


import qrcode


print('Bem-vindo ao meu gerador de Qr code para Wi-Fi\n')

def Nome_Da_Rede():     #Função para ver se o nome da rede está correto e retornar o nome da rede.
    nomedarede = input('Digite aqui o nome exato da sua rede Wi-Fi (SSID): ')        
    print(f'O nome da sua rede Wi-Fi é : {nomedarede}')
    correto = input('Está correto? S/N\n')
    correto = correto.upper()
    if correto == 'S':
        pass
    elif correto == 'N':
        Nome_Da_Rede()
    else:
        print('Não entendi')
        Nome_Da_Rede()
    return nomedarede


def Senha():     #Função para definir a senha
    senha = input('Digite aqui a sua senha: ')        
    print(f'Essa é sua senha: {senha}')
    correto = input('Está correta? S/N\n')
    correto = correto.upper()
    if correto == 'S':
        pass
    elif correto == 'N':
        Senha()
    else:
        print('Não entendi')
        Senha()
    return senha


def Gerar_Link():       #Irá gerar a configuração do WI-FI e retornar os valores parar criar o código QR
    tipo = input('Digite aqui o tipo de sua rede (WEP ou WPA): ')
    tipo = tipo.upper()
    if tipo == 'WEP':
        tipo = 'WEP'
    elif tipo == 'WPA':
        tipo = 'WPA'
    else: 
        print('Não entendi, vamos começar de novo.\n\n')
        Gerar_Link()

    nomedarede = Nome_Da_Rede()
    senha = Senha()

    return tipo,nomedarede,senha

   
def Cria_Código_qr(tipo,nomedarede,senha):       #Gerar e salvar o código QR
    qr = qrcode.make(f'WIFI:T:{tipo};S:{nomedarede};P:{senha};H:;')
    qr.save(f'Qr_Code_Wifi.png')

##CHAMADA DAS FUNÇÕES / INICIO DO PROGRAMA
tipo,nomedarede,senha = Gerar_Link()
Cria_Código_qr(tipo,nomedarede,senha)


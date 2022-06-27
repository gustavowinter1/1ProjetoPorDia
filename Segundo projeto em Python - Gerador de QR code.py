##Segundo projeto em Python
#@Gerador de QR Code

#qr = qrcode.make('Aqui é o link ou texto, numero a ser gerado o QR Code')       
#qr.save('#Aqui é o nome do arquivp ++ extensão,, ex: teste.png') 

import qrcode


def GeraQR():
    link = input('Digite aqui o link para gerar o QR code (Para encerrar digite 0): ')
    if link == '0':
        exit(print('Obrigado por usar o gerador de QR Code!'))
    else:
        qr = qrcode.make(f'{link}')     #Código para inserir link ou texto ex:  qr = qrcode.make('Teste')
        nome = input('Digite aqui o nome para salvar o seu qr code: ') 
        qr.save(f'{nome}.png')      #Código para salvar o arquivo seguido da extensão, por padrão deixei .png



while True:
    GeraQR()
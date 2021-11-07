import qrcode

from funcao2 import EscrevendoSite, EscrevendoTexto

deseja =input('A parte[1] criar QR de site [2] para criar QR de um Texto:')
if deseja == '1':
    site = input('digite o site:')
    EscrevendoSite(site)
else:
    texto = input('insirar o texto:')
    EscrevendoTexto(texto)


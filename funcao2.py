import qrcode

def EscrevendoSite(site):
    # usado para o site
    img = qrcode.make(site)
    
    img.save("some_file1.png")

def EscrevendoTexto(texto):
    # usado para da uma menssagem 
    img = qrcode.make(texto)

    type(img)  # qrcode.image.pil.PilImage
    img.save("some_file2.png")

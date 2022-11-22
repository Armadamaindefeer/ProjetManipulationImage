def noirEtBlanc(input):
    from PIL import Image
    img = Image.open(input)
    hauteur_image = img.height
    largeur_image = img.width
    for y in range(hauteur_image):
        for x in range(largeur_image):
            r,v,b=img.getpixel((x,y))
            gris = (r+v+b) // 3
            if gris >128:
                img.putpixel((x,y), (255,255,255))
            else:
                img.putpixel((x,y), (0,0,0))
    img.save("output/gris.png")
    img.show()
from PIL import Image
img = Image.open("pomme.png")
r,v,b=img.getpixel((271,142))
print("canal rouge : ",r,"canal vert : ",v,"canal bleu : ",b)
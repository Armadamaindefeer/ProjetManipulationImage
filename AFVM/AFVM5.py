from PIL import Image
img = Image.open("pomme.png")
for y in range(200, 250):
  for x in range(260,295):
    img.putpixel((x,y), (255,0,0))
img.show()
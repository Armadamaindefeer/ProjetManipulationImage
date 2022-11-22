from PIL import Image
img = Image.open("pomme.png")
img = img.transpose(Image.ROTATE_270)
img.save("output/pomme_90_degrés_r.png")
img.show()

from PIL import Image
import numpy as np

im = Image.open('data/img.jpeg')

# holen der grundsaetzlichen Eigenschaften des Bildes:
breite, hoehe = im.size
print("breite: %s , hoehe: %s"  % (breite, hoehe))
print("palette: %s" % im.palette)
print("format: %s" % im.format)
print("mode: %s" % im.mode)

imr = im.rotate(45) # Gibt das rotierte Bild zurueck
imr.save('data/rotated.jpeg')

im.thumbnail( (128,128) )  # Die Methode verändert im
im.save('data/thumb.jpeg')
#im.show()

a = np.asarray(im)
#print(a)

img = Image.fromarray(a)


k = im.info.keys()
print(k)

for k in im.info.keys():
    print("%s : %s" % (k, im.info[k]))
from PIL import Image

pics = []

#comment
for i in range(1, 10):
    j = str(i) + '.png'
    pics.append(Image.open(j))

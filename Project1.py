from PIL import Image
import statistics

images = []

for i in range(1, 10):
    img = Image.open('C:/Users/lolib/Dropbox/CST205P1/' + str(i) + '.png')
    images.append(img)

#images[0].show()

pixels = []
final = []

for i in range(0, 9):
    pixels.append([])

for k in range(0, 9):
    for i in range(0, 494):
        for j in range(0, 556):
            r, g, b = images[k].getpixel((i,j))
            pixels[k].append((r,g,b))

for i in range(len(pixels[0])):
    temp = [pixels[0][i], pixels[1][i], pixels[2][i], pixels[3][i], pixels[4][i], pixels[5][i], pixels[6][i], pixels[7][i], pixels[8][i]]
    final.append(statistics.median(sorted(temp)))

new = Image.new('RGB', (495,557), 0)

pix = new.load()

k = 0
for i in  range(0, 494):
    for j in range(0, 556):
        pix[i, j] = final[k]
        k += 1
new.show()

from PIL import Image
import statistics

images = []

#Open all images and throw them in a list
for i in range(1, 10):
    img = Image.open('C:/Users/lolib/Dropbox/CST205P1/' + str(i) + '.png')
    images.append(img)

pixels = []
final = []
xSize, ySize = img.size

#Create 2D list for pixels
for i in range(0, 9):
    pixels.append([])

#Grab all the pixels and tuple them into the 2D list
for k in range(0, 9):
    for i in range(0, xSize):
        for j in range(0, ySize):
            r, g, b = images[k].getpixel((i,j))
            pixels[k].append((r,g,b))

#Grab the same pixels from all images, sort them and get the median
for i in range(len(pixels[0])):
    temp = [pixels[0][i], pixels[1][i], pixels[2][i], pixels[3][i], pixels[4][i], pixels[5][i], pixels[6][i], pixels[7][i], pixels[8][i]]
    final.append(statistics.median(sorted(temp)))

#Create new image
new = Image.new('RGB', (xSize,ySize), 0)

pix = new.load()

#Put all the correct pixels into the new image
k = 0
for i in  range(0, xSize):
    for j in range(0, ySize):
        pix[i, j] = final[k]
        k += 1

#print the image
new.show()

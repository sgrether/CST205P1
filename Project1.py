from PIL import Image
import statistics

images = []
num = int(input('Enter number of images:'))
#Open all images and throw them in a list
for i in range(1, num+1):
    images.append(Image.open(str(i) + '.png'))

pixels = []
final = []
xSize, ySize = images[0].size

#Create 2D list for pixels
for i in range(0, num):
    pixels.append([])

#Grab all the pixels and tuple them into the 2D list
for k in range(0, num):
    for i in range(0, xSize):
        for j in range(0, ySize):
            temp = images[k].getpixel((i,j))
            pixels[k].append(temp)

#Grab the same pixels from all images, sort them and get the median
for i in range(len(pixels[0])):
    temp = []
    for j in range(0, num):
        temp.append(pixels[j][i])
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
inp = input('1. Show Image\n2. Save Image\n')
if(inp == '1'):
    #print the image
    new.show()
if(inp == '2'):
    #Save image as png
    new.save('NewImage.png', 'PNG')

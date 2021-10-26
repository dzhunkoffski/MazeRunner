from PIL import Image

img = Image.open("B.bmp")
pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        if pixels[i, j] != (0, 0, 0) and pixels[i, j] != (255, 255, 255):
            pixels[i, j] = (255, 255, 255)
img.show()
img.save('maze.png', '')

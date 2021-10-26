import cv2
from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt
import numpy as np
import bfs_solver

# Ввод фотографии, которая преобразовывается:
print('Put maze image into program directory and write down its name: ', end='')
imageName = input()
img = Image.open(imageName)
pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        if pixels[i, j] < (192, 192, 192):
            pixels[i, j] = (0, 0, 0)
        else:
            pixels[i, j] = (255, 255, 255)

img.save('maze.png', '')
print("MAZE SAVED")

# Resizing
base_width = 100
ratio = (base_width / float(img.size[0]))
height = int(float(img.size[1]) * float(ratio))
img = img.resize((base_width, height), Image.ANTIALIAS)
pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        if pixels[i, j] < (192, 192, 192):
            pixels[i, j] = (0, 0, 0)
        else:
            pixels[i, j] = (255, 255, 255)

img.save('resized_maze.png', '')
print("MAZE RESIZED")

img1 = cv2.imread('resized_maze.png')
plt.imshow(img1)
plt.show()

check1 = False
check2 = False
print("Enter start_point coords:")
while not check1:
    s_x, s_y = map(int, input().split())
    if pixels[s_x, s_y] != (0, 0, 0):
        start_point = [s_x, s_y]
        check1 = True
    else:
        print("You can not choose wall as a start_point")
print("Enter finish_point coords:")
while not check2:
    f_x, f_y = map(int, input().split())
    if pixels[f_x, f_y] != (0, 0, 0):
        finish_point = [f_x, f_y]
        check2 = True
    else:
        print("You can not choose wall as a finish_point")

cv2.circle(img1, (s_x, s_y), 1, (0, 255, 0), -1)
cv2.circle(img1, (f_x, f_y), 1, (255, 0, 0), -1)
plt.figure(figsize=(4, 4))
plt.show()

maze_binary = np.full((img.size[0], img.size[1]), 0)
for i in range(0, img.size[0]):
    for j in range(0, img.size[1]):
        if pixels[i, j] == (0, 0, 0):
            maze_binary[i, j] = int(1)
        else:
            maze_binary[i, j] = int(0)
print("BINARY MAZE CREATED")
np.savetxt('maze_binary.txt', maze_binary, delimiter='')

size_x = img.size[0]
size_y = img.size[1]

path = bfs_solver.solve(maze_binary, start_point, finish_point, size_x, size_y)
print(path)
print("PATH_DONE")
for dots in path:
    i = dots[0]
    j = dots[1]
    pixels[i, j] = (0, 0, 255)
img.show()
img.save('solved_maze.png', '')
print("MAZE SUCCESSFULY SOLVED AS solved_maze.png")

img3 = cv2.imread('solved_maze.png')
cv2.circle(img3, (s_x, s_y), 2, (0, 255, 0), -1)
cv2.circle(img3, (f_x, f_y), 2, (255, 0, 0), -1)
plt.figure(figsize=(4, 4))
plt.imshow(img3)
plt.show()

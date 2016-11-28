#!/usr/bin/env python
# -- coding: utf-8 --
from PIL import Image
im = Image.open("PIL_test2.png")
pix = im.load()

ans = Image.new("RGB", (im.size[0], im.size[1]), "white")
de = ans.load()
green = (0, 209, 0, 255)
red = (255, 0, 0, 255)
yellow = (255, 247, 0, 255)
blue = (21, 0, 255, 255)
pink = (255, 0, 204, 255)

colors = []
for y in range(0,im.size[0]):
	b = []
	for x in range(0,im.size[1]):
		b.append(pix[x,y])
	colors.append(b)

measurements = [green,green,blue]
motions = [[0,0],[1,0],[0,1]]

sensor_right = 1.0

p_move = 1.0

def show(p):
    for i in range(len(p)):
        print p[i]


sensor_wrong = 1.0 - sensor_right
p_stay = 1.0 - p_move
def sense(p,colors, measurement):
    aux = [[0.0 for row in range(0,len(p[0]))] for col in range(0,len(p))]
    s = 0.0
    for i in range(0,len(p)):
        for j in range(0,len(p[i])):
            hit = (measurement == colors[i][j])
            aux[i][j] = p[i][j] * (hit * sensor_right + (1-hit) * sensor_wrong)
            s += aux[i][j]    
    for i in range(0,len(aux)):
        for j in range(len(p[i])):
            aux[i][j] /= s
    return aux


def move(p, U):
    aux = [[0.0 for row in range(0,len(p[0]))] for col in range(0,len(p))]
    for i in range(0,len(p)):
        for j in range(0,len(p[i])):
            aux[i][j] = (p_move * p[(i - U[0]) % len(p)][(j - U[1]) % len(p[i])]) + (p_stay * p[i][j])   
    return aux
pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
p = [[pinit for row in range(0,len(colors[0]))] for col in range(0,len(colors))]

for x in range(0,len(measurements)):
    p = move(p, motions[x])
    p = sense(p, colors, measurements[x])
    
for i in range(0,len(p)):
    for j in range(0,len(p[i])):
        de[j,i] = (255-int(pix[j,i][0]*p[i][j]),255-int(pix[j,i][1]*p[i][j]),int(pix[j,i][2]*p[i][j]),int(pix[j,i][3]*p[i][j]))
ans.save("ans.png", "PNG")

show(p)


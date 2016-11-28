#!/usr/bin/env python
# -- coding: utf-8 --
colors = [['red', 'green', 'green',   'red', 'red'],
          ['red',   'red', 'green',   'red', 'red'],
          ['red',   'red', 'green', 'green', 'red'],
          ['red',   'red',   'red',   'red', 'red'],
	  ['greeb', 'red', 'green',  'red','green']]

measurements = ['green', 'green', 'green' ,'green', 'green','red']

"""p = [[1./20, 1./20, 1./20, 1./20, 1./20],
     [1./20, 1./20, 1./20, 1./20, 1./20],
     [1./20, 1./20, 1./20, 1./20, 1./20],
     [1./20, 1./20, 1./20, 1./20, 1./20]]"""

motions = [[0,0],[0,1],[1,0],[1,0],[0,1],[-1,0]]

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
    

show(p)



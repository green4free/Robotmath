#!/usr/bin/env python
# -- coding: utf-8 --
# -----------
# User Instructions:
# 
# Modify the function search so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# Make sure that the initial cell in the grid 
# you return has the value 0.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    p = [0]+init
    o = [p]
    c = [p]
    ex = [[int(-1) for row in range(len(grid[0]))] for col in range(len(grid))]
    while p[1:] != goal:
        for u in delta:
            if not((p[1]+u[0] < 0 or p[1]+u[0] > len(grid)-1) or (p[2]+u[1] < 0 or p[2]+u[1] > len(grid[0])-1)):
                if grid[p[1]+u[0]][p[2]+u[1]] != 1:
                    r = 0
                    for t in o:
                        if t[1:] == [p[1]+u[0],p[2]+u[1]]:
                            r = 1
                            break
                    if r != 1:
                        o.append([p[0]+1]+[p[1]+u[0],p[2]+u[1]])
                        c.append([p[0]+1]+[p[1]+u[0],p[2]+u[1]])
        c.remove(p)
        if len(c) == 0:
            break
        c.sort(key=lambda x: int(x[0]))
        p = c[0]
    for i in range(len(o)):
        for tt in ex:
            print tt
        print o[i], "\n"
        ex[o[i][1]][o[i][2]] = i
    return ex

print search(grid,init,goal,cost)


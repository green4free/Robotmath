#!/usr/bin/env python
# -- coding: utf-8 --
# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 0],
	[0, 0, 1, 0, 0, 0, 1, 0]]
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
            p = "fail"
            break
        c.sort(key=lambda x: int(x[0]))
        p = c[0]
    return p
print search(grid,init,goal,cost)

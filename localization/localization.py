#!/usr/bin/env python
# -- coding: utf-8 --
#Det är en 1-dimensionell lopande värld, en robot rör sig genom den
#Variabeln world beskriver den världen
#Variabeln measurements beskriver vad roboten ser
#Variabeln motions beskriver hur roboten rör sig
#Programmet skriver ut sannolikheten för robotens position
#funktionen move räknar med felkällan i exaktheten på hur roboten rör sig

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'green', 'red', 'green', 'red']
measurements = ['red', 'red','green']
motions = [1,1,1]
pHit = 0.9
pMiss = 0.1
pExact = 1.0
pOvershoot = 0
pUndershoot = 0

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def topped(a, p):
	if a <= len(p) - 1:
		return a
	else:
		return len(p) - 1

def move(p, U):
    q = [0,0,0,0,0]
    for i in range(len(p)):
        q[i] += pExact * p[topped(i-U, p) ]
    return q
"""
for x in range(len(measurements)):
    p = sense(p, measurements[x])
    p = move(p, motions[x])
print p   
"""
p = sense(p, 'red')
p = move(p, 1)
print sense(p, 'red')   

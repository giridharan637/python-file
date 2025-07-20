
n = int(input('Enter n:'))
for i in range(n):
    for j in range(n):
        if(i==j or j == n-1-i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
"""
n = int(input("Enter n:"))
for i in range(n):
    for j in range(n):
        if((i == 0 or i == n-1) and (j!=0 and j!=n-1)):
            print("*",end=" ")
        elif((j == 0 or j == n-1) and (i!=0 and i!=n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
     

n =  int(input())

for i in range(n):
    for j in range((2 * n) - 1):
        if (j == n - i - 1) or (j == n + i - 1) or (i == n // 2 and j > n - i - 1 and j < n + i - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()
 
from turtle import *
import colorsys

speed(0)
bgcolor("black")
h = 0

for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h += 0.005

        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)

    circle(40, 24)

done()
   """



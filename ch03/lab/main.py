import turtle #1. import modules
import random
import pygame
import math

num_steps = 10
coords = []
num_sides = 3
side_length = 100
offset = 100
size = [5000, 5000]
bg_color = ('black')

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here

michelangelo.forward(random.randrange(1,100))
leonardo.forward(random.randrange(1,100))

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

for x in range(num_steps + 1):
  michelangelo.forward(random.randrange(1,10))
  leonardo.forward(random.randrange(1,10))
  
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)



# PART B - complete part B here

pygame.init()
window = pygame.display.set_mode(size)

for q in range(5): #five shapes i have to draw
  coords = [] #reset coords so new coords can be calculated
  for n in range(num_sides):
    theta = (2.0 * math.pi * n) / num_sides
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    coords.append((x,y))
#print(coords)
  pygame.draw.polygon(window, 'blue', coords)
  pygame.display.flip()
  pygame.time.wait(1000)
  window.fill(bg_color)
  pygame.display.flip()

  if num_sides == 3: #goes to next shape depending on current shape
    num_sides = 4
  elif num_sides == 4:
    num_sides = 6
  elif num_sides == 6:
    num_sides = 9
  else:
    num_sides = 360
  

#window.exitonclick()

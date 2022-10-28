import turtle
myturtle = turtle.Turtle()


def main():
  num_layers = (int(input("how many layers should the pyramid be?")))
  scale = 2
  offset_y = -30
  bg_color = "black"
  brick_width = 10*scale
  brick_height = 5*scale
  turtle.screensize(200,150)
  window = turtle.Screen()
  window.bgcolor(bg_color)
  myturtle.color('white')
  myturtle.shape('turtle')
  myturtle.pu()
  
  for layer in range(0, num_layers):
    myturtle.goto(layerCoords(num_layers, layer, brick_width, brick_height, offset_y))
    for brick in range(0, (num_layers - layer)):
      drawBrick(brick_width, brick_height)

  turtle.exitonclick()
def drawBrick(brick_width=None, brick_height=None):
  
  '''
   draws an individual brick, and then moves the turtle in place to draw the next brick
   
   args: 
   (int) brick_width - the width of each individual brick being drawn
   (int) brick_height - the height of each individual brick being drawn
   
   return:
   None
   '''
  
  myturtle.pd()
  
  myturtle.forward(brick_width)
  myturtle.left(90)
  myturtle.forward(brick_height)
  myturtle.left(90)
  myturtle.forward(brick_width)
  myturtle.left(90)
  myturtle.forward(brick_height)
  myturtle.left(90)
  
  myturtle.pu()
  myturtle.forward(brick_width)
  
def layerCoords(num_layers=None, layernum=None, brick_width=None, brick_height=None, offset_y=0):
  
  '''
   determines and returns the coordinate pair that the turtle has to go to next, in order to start drawing the next layer up.
   
   args:
   (int) num_layers: number of layers total in the pyramid
   (int) layernum: the current layer the turtle is drawing
   (int) brick_width: the width of each individual brick being drawn
   (int) brick_height: the height of each individual brick being drawn
   (int) offset_y: the offset in the y direction used in calculating the coordinate pairs so that the pyramid is in the middle of the screen
   
   return: 
   tuple (int, int): the new coordinates of the turtle
   '''
  
  new_turtle_x = (-(0.5*brick_width*(num_layers-layernum)))
  new_turtle_y = (offset_y + (layernum*brick_height))
  return(new_turtle_x,new_turtle_y)


main()
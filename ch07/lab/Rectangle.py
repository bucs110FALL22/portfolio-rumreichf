class Rectangle:
  def __init__(self, x=0, y=0, h=0, w=0):
    if x >= 0:
      self.x = x
    else:
      self.x = 0
    if y >= 0:
      self.y = y
    else:
      self.y = 0
    if h >= 0:
      self.height = h
    else:
      self.height = 0
    if w >= 0:
      self.width = w
    else:
      self.width = 0

  def __str__(self):
     return f"x: {self.x}, y: {self.y}, height: {self.height}, width: {self.width}"


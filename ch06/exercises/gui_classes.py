class Player:
  def __init__(self):
    self.player_num = 1
    self.lives = 3
    self.is_large = False

class Enemy:
  def __init__(self):
    self.enemy_type = "goomba"
    self.speed = 1
    self.direction_moving = "left"

class MysteryBlock:
  def __init__(self):
    self.contents = "coin"
    self.is_used = False
    self.height = 4


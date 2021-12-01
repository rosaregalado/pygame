import pygame
from random import randint, choice

# import classes and lanes
from GameObject import GameObject
from constants import lanes_x, lanes_y

# create Apple class
class Apple(GameObject):
  def __init__(self):
    super(Apple, self).__init__(0, 0, 'images/apple.png')
    self.dx = 0
    self.dy = (randint(0, 200) / 100) + 1
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.y > 600:
      self.reset()

  def reset(self):
    self.x = choice(lanes_x)
    self.y = -64
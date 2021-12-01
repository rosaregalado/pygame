import pygame
from random import randint, choice

# import classes and lanes
from GameObject import GameObject
from constants import lanes_x, lanes_y


class Strawberry(GameObject):
  def __init__(self):
    super(Strawberry, self).__init__(0, 0, 'images/strawberry.png')
    self.dx = (randint(0, 200) / 100) + 1
    self.dy = 0
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.x > 700:
      self.reset()

  def reset(self):
    self.x = -64
    self.y = choice(lanes_y)

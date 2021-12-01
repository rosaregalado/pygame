import pygame
from random import randint, choice

#import classes and lanes
from GameObject import GameObject
from constants import lanes_x, lanes_y


class Player(GameObject):
	def __init__(self):
		super(Player, self).__init__(0, 0, 'images/player.png')
		self.dx = 0
		self.dy = 0
		self.pos_x = 1 # new attribute
		self.pos_y = 1 # new attribute
		self.reset()

	def left(self):
		if self.pos_x > 0:
			self.pos_x -= 1
			self.update_dx_dy()

	def right(self):
		if self.pos_x < len(lanes_x) - 1:
			self.pos_x += 1
			self.update_dx_dy()

	def up(self):
		if self.pos_y > 0:
			self.pos_y -= 1
			self.update_dx_dy()

	def down(self):
		if self.pos_y < len(lanes_y) - 1:
			self.pos_y += 1
			self.update_dx_dy()

	def move(self):
		self.x -= (self.x - self.dx) * 0.25
		self.y -= (self.y - self.dy) * 0.25

	def reset(self):
		self.x = lanes_x[self.pos_x]
		self.y = lanes_y[self.pos_y]
		self.dx = self.x
		self.dy = self.y

	def update_dx_dy(self): 
		#keeps player in the available lanes
		self.dx = lanes_x[self.pos_x]
		self.dy = lanes_y[self.pos_y]


import pygame

class piece():
	def __init__(self , pos_piece , color , name):
		self.pos = pos_piece
		self.color = color
		self.name = name

	def get_valid_move(self):
		pass

	def move(self , board):
		pass

	def draw(self , display):
		display.blit(self.img , (self.pos[1] * 80 + 300, self.pos[0] * 80))
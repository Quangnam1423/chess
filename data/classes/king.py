import pygame
from data.classes.Piece import piece

class king(piece):
	def __init__(self , pos_piece , color , name):
		super().__init__(pos_piece , color , name)
		img_path = 'data/imgs/' + name + '.png'
		self.img = pygame.transform.scale(pygame.image.load(img_path) , (80 , 80))
		self.notation = 'k'

	def get_possible_move(self , board):
		pass

	
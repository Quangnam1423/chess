import pygame
from data.classes.Piece import piece

class king(piece):
	def __init__(self , pos_piece , color , name):
		super().__init__(pos_piece , color , name)
		img_path = 'data/imgs/' + name + '.png'
		self.img = pygame.transform.scale(pygame.image.load(img_path) , (80 , 80))
		self.notation = 'k'

	def get_possible_move(self , board_config):
		output = []
		moves = [
			(- 1 , -1) , (-1 , 0) , 
			(-1 , 1) , (0 , -1) , 
			(0 , 1) , (1 , -1) ,
			(1 , 0) , (1 , 1)
		]
		for move in moves:
			if self.pos[0] + move[0] > 7 or self.pos[0] + move[0] < 0 \
			or self.pos[1] + move[1] > 7 or self.pos[1] + move[1] < 0:
				continue
			if board_config[self.pos[0] + move[0]][self.pos[1] + move[1]][0] != self.color:
				output.append((self.pos[0] + move[0] , self.pos[1] + move[1]))

		return output

	def can_castle(self , gs):
		#if self.has_move == False and 
		pass
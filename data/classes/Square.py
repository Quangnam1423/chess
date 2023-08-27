import pygame

class square():
	def __init__(self , x , y):
		self.current_piece = None
		self.pos_config = (x , y)
		self.size = 80
		self.abs_x = y * 80
		self.abs_y = x * 80
		self.highlight = False

		self.rect = pygame.Rect(
			self.abs_x,
			self.abs_y,
			self.size,
			self.size
		)
		self.highlight_color = None
		self.coord = self.get_coord()

	def get_coord(self):
		columns = 'abcdefgh'
		return columns[self.pos_config[0]] + str(self.pos_config[1] + 1)

	def draw(self , display):
		if self.current_piece != None:
			self.current_piece.draw(display)
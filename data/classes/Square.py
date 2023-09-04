import pygame

class square():
	def __init__(self , x , y):
		self.piece = None
		self.pos_config = (x , y)
		self.x = x
		self.y = y
		self.size = 80
		self.abs_x = y * 80 + 300
		self.abs_y = x * 80

		self.rect = pygame.Rect(
			self.abs_x,
			self.abs_y,
			self.size,
			self.size
		)
		self.rect.center = self.abs_x + 40 , self.abs_y + 40
		self.highlight = False
		self.highlight_color = (124 , 0 , 100)
		self.coord = self.get_coord()
		self.click = False

	def get_coord(self):
		columns = 'abcdefgh'
		return columns[self.pos_config[0]] + str(self.pos_config[1] + 1)

	def check_collidepoint(self , e_pos):
		if self.rect.collidepoint(e_pos):
			return True
		return False

	def draw(self , display):
		if self.highlight == True:
			display.draw.rect(display , self.highlight_color , self.rect)
		if self.piece != None and not self.click:
			self.piece.draw(display)

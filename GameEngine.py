'''
This class will be responsible for storing all the imformation about the current state of a chess game.
It will be also responsible for determining the valid moves at the current state.It will be also keep the move log.
'''
import pygame
from data.classes.bishop import bishop
from data.classes.rook import rook
from data.classes.knight import knight
from data.classes.queen import queen
from data.classes.king import king
from data.classes.pawn import pawn
from data.classes.Square import square

class GameState():
	def __init__(self , boardsize):
		self.length = boardsize[0]
		self.width = boardsize[1]
		self.SquareSize = self.length // 8
		'''
		Board is an 8 x 8 2D list, each element of the list has two charater.
		The first charater represents the color of the piece ('b' of 'w').
		The second charater represents for the type of the piece('k' , 'q' , 'k' , 'n' ...)
		'--' respresents for the empty space with no piece

		'''
		self.config = [
			['br' , 'bn' , 'bb' , 'bq' , 'bk' , 'bb' , 'bn' , 'br'],
			['bp' , 'bp' , 'bp' , 'bp' , 'bp' , 'bp' , 'bp' , 'bp'],
			['--' , '--' , '--' , '--' , '--' , '--' , '--' , '--'],
			['--' , '--' , '--' , '--' , '--' , '--' , '--' , '--'],
			['--' , '--' , '--' , '--' , '--' , '--' , '--' , '--'],
			['--' , '--' , '--' , '--' , '--' , '--' , '--' , '--'],
			['wp' , 'wp' , 'wp' , 'wp' , 'wp' , 'wp' , 'wp' , 'wp'],	
			['wr' , 'wn' , 'wb' , 'wq' , 'wk' , 'wb' , 'wn' , 'wr'],		
		]
		self.turn = 'white'
		self.squares = self.generate_square()
		self.board = pygame.transform.scale(pygame.image.load('data/imgs/Chessboard.png') , boardsize)
		self.board.convert()
		self.setup_board()


	def generate_square(self):
		squares = []
		for i in range(8):
			for j in range(8):
				squares.append(
					square(i , j)
				)
		return squares

	def get_square_from_pos(self , pos):
		for square in self.squares:
			if square.pos_config == pos:
				return square


	def setup_board(self):
		for i , row in enumerate(self.config):
			for j , piece in enumerate(row):
				square = self.get_square_from_pos((i , j))
				if piece != '--':
					if piece[1] == 'r':
						square.current_piece = rook(
							(i , j) , 'white' if piece[0] == 'w' else 'black' , piece
						)

					elif piece[1] == 'n':
						square.current_piece = knight(
							(i , j) , 'white' if piece[0] == 'w' else 'black' , piece
						)

					elif piece[1] == 'b':
						square.current_piece = bishop(
							(i , j) , 'white' if piece[0] == 'w' else 'black' , piece
						)

					elif piece[1] == 'q':
						square.current_piece = queen(
							(i , j) , 'white' if piece[0] == 'w' else 'black' , piece
						)

					elif piece[1] == 'k':
						square.current_piece = king(
							(i , j) , 'white' if piece[0] == 'w' else 'black' , piece
						)

					elif piece[1] == 'p':
						square.current_piece = pawn(
							(i , j) , 'white' if piece[0] == 'w' else 'black' , piece
						)


	def draw_board(self , display):
		display.blit(self.board , (300 , 0))
		for square in self.squares:
			square.draw(display)
	
	def handle_the_click(self):
		pass

	def checkmate(self):
		pass


'''
	def DrawPiece(self , screen , Images):
		for y, row in enumerate(self.config):
			for x, piece in enumerate(row):
				if piece != '--':
					screen.blit(Images[piece] , \
					pygame.Rect(200 + x * self.square_size , y * self.square_size , self.square_size , self.square_size))
'''
'''
	def DrawPiece(self , screen , Images):
		for i in range(8):
			for j in range(8):
				if self.config[i][j] != '--':
					screen.blit(Images[self.config[i][j]] , \
						(300 + j * self.square_size , i * self.square_size , self.square_size , self.square_size))
'''
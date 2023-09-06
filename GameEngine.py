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
		self.turn = 'w'
		self.squares = self.generate_square()
		self.board = pygame.transform.scale(pygame.image.load('data/imgs/Chessboard.png') , boardsize)
		self.board.convert()
		self.setup_board()
		self.checking = False
		self.bk_pos = (0 , 4)
		self.wk_pos = (7 , 4)
		self.can_check_mate = self.is_in_check()
		self.checkmate = False


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
			if square.pos == pos:
				return square

	def get_square_from_mouse(self , mouse_pos):
		for square in self.squares:
			if square.check_collidepoint(mouse_pos):
				return square


	def setup_board(self):
		for i , row in enumerate(self.config):
			for j , piece in enumerate(row):
				square = self.get_square_from_pos((i , j))
				if piece != '--':
					if piece[1] == 'r':
						square.piece = rook(
							(i , j) , 'w' if piece[0] == 'w' else 'b' , piece
						)

					elif piece[1] == 'n':
						square.piece = knight(
							(i , j) , 'w' if piece[0] == 'w' else 'b' , piece
						)

					elif piece[1] == 'b':
						square.piece = bishop(
							(i , j) , 'w' if piece[0] == 'w' else 'b' , piece
						)

					elif piece[1] == 'q':
						square.piece = queen(
							(i , j) , 'w' if piece[0] == 'w' else 'b' , piece
						)

					elif piece[1] == 'k':
						square.piece = king(
							(i , j) , 'w' if piece[0] == 'w' else 'b' , piece
						)

					elif piece[1] == 'p':
						square.piece = pawn(
							(i , j) , 'w' if piece[0] == 'w' else 'b' , piece
						)
				else:
					square.piece = None


	def draw_board(self , display , click_piece , click_piece_rect):
		display.blit(self.board , (300 , 0))
		for square in self.squares:
			square.draw(display)
		if click_piece is not None:
			display.blit(click_piece.img , click_piece_rect)

			
	def handle_the_click(self , pos_down , pos_up ,possible_move):
		clicked_sq = self.get_square_from_mouse(pos_down)
		if clicked_sq.piece == None:
			return
		print(id(clicked_sq.piece))
		x = clicked_sq.pos
		clicked_sq.click = False
		select_sq = self.get_square_from_mouse(pos_up)
		if clicked_sq is select_sq or clicked_sq == None or select_sq == None:
			clicked_sq.click = False
			self.erase_highlight(possible_move)
			return

		y = select_sq.pos
		if self.checkmate == False:
			if any(i == select_sq.pos for i in possible_move):
				select_sq.piece , clicked_sq.piece = clicked_sq.piece , None
				select_sq.piece.pos = select_sq.pos
				self.config[x[0]][x[1]] , self.config[y[0]][y[1]] = '--' , self.config[x[0]][x[1]]
				select_sq.piece.has_move = True
				if select_sq.piece.name[1] == 'k':
					if self.turn == 'w':
						self.wb_pos = select_sq.pos
					else:
						self.bk_pos = select_sq.pos
				self.turn = 'w' if self.turn == 'b' else 'b'

			self.erase_highlight(possible_move)
			possible_move = None
		else:
			pass
		return

	def fill_highlight(self , moves):
		for move in moves:
			square = self.get_square_from_pos(move)
			if square.piece != None and square.piece.color != self.turn:
				square.attacked = True
			else:
				square.highlight = True
		return

	def erase_highlight(self , moves):
		for move in moves:
			square = self.get_square_from_pos(move)
			square.highlight = False
			square.attacked = False


	def is_in_check(self):
		output = []
		for sq in self.squares:
			if sq.piece != None and sq.piece.color != self.turn:
				output += sq.piece.get_possible_move(self.config)
		return output

	def checking_mate(self):
		if self.turn == 'w':
			if any(i == self.wk_pos for i in self.can_check_mate):
				self.checkmate = True
				return
		else:
			if any(i == self.bk_pos for i in self.can_check_mate):
				self.checkmate = True
				return
		self.checkmate = False
		return

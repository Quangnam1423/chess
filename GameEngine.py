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
		x = clicked_sq.pos
		clicked_sq.click = False
		select_sq = self.get_square_from_mouse(pos_up)
		if clicked_sq is select_sq or clicked_sq == None or select_sq == None:
			clicked_sq.click = False
			self.erase_highlight(possible_move)
			return
		y = select_sq.pos
		if any(i is select_sq for i in possible_move):
			if clicked_sq.piece.notation == 'k' and abs(x[1] - y[1]) == 2:
				rook_square , new_rook_square = None , None
				if x[1] > y[1]:
					rook_square = self.get_square_from_pos((x[0] , 0))
					new_rook_square = self.get_square_from_pos((x[0] , 3))
				else:
					rook_square = self.get_square_from_pos((x[0] , 7))
					new_rook_square = self.get_square_from_pos((x[0] , 5))
				h = rook_square.pos
				k = new_rook_square.pos
				select_sq.piece , clicked_sq.piece = clicked_sq.piece , None
				select_sq.piece.pos = select_sq.pos
				self.config[x[0]][x[1]] , self.config[y[0]][y[1]] = '--' , self.config[x[0]][x[1]]	
				rook_square.piece , new_rook_square.piece = None , rook_square.piece
				new_rook_square.piece.pos = new_rook_square.pos
				self.config[h[0]][h[1]] , self.config[k[0]][k[1]] = '--' , self.config[h[0]][h[1]]
				new_rook_square.piece.has_move , select_sq.piece.has_move = True , True
			else:
				select_sq.piece , clicked_sq.piece = clicked_sq.piece , None
				select_sq.piece.pos = select_sq.pos
				self.config[x[0]][x[1]] , self.config[y[0]][y[1]] = '--' , self.config[x[0]][x[1]]
				select_sq.piece.has_move = True
			self.turn = 'w' if self.turn == 'b' else 'b'
		self.erase_highlight(possible_move)
		possible_move = None
		return

	def fill_highlight(self , possible_move):
		for square in possible_move:
			if square.piece != None and square.piece.color != self.turn:
				square.attacked = True
			else:
				square.highlight = True
		return

	def erase_highlight(self , squares):
		for square in squares:
			square.highlight = False
			square.attacked = False
		return

	def is_in_check(self):
		output = []
		for sq in self.squares:
			if sq.piece != None and sq.piece.color != self.turn:
				output += sq.piece.get_possible_move(self.config , self.squares)
		return output

	def checking_mate(self):
		if self.turn == 'w':
			if any(i.pos == self.wk_pos for i in self.can_check_mate):
				self.checkmate = True
				return
		else:
			if any(i.pos == self.bk_pos for i in self.can_check_mate):
				self.checkmate = True
				return
		self.checkmate = False
		return

	def get_king_pos(self):
		pieces = [i.piece for i in self.squares if i.piece is not None]
		for piece in pieces:
			if piece.notation == 'k' and piece.color == self.turn:
				if self.turn == 'w':
					self.wk_pos = piece.pos
				else:
					self.bk_pos = piece.pos
		return

	def checkLegalMove(self , clicked_pos , select_pos):
		output = True
		king_pos = None
		changing_piece = None
		old_square = None
		new_square = None
		new_square_old_piece = None
		temp = None
		x = None
		y = None
		for square in self.squares:
			if square.pos == clicked_pos:
				old_square = square
				changing_piece = old_square.piece
				old_square.piece = None
				x = old_square.pos
				break
		for square in self.squares:
			if square.pos == select_pos:
				new_square = square
				y = new_square.pos
				new_square_old_piece = new_square.piece
				new_square.piece = changing_piece
				changing_piece.pos = new_square.pos
				temp = self.config[y[0]][y[1]]
				self.config[y[0]][y[1]] = self.config[x[0]][x[1]]
				self.config[x[0]][x[1]] = '--'
				break
		pieces_atk = [i.piece for i in self.squares if i.piece is not None and i.piece.color != self.turn]
		pieces = [i.piece for i in self.squares if i.piece is not None and i.piece.color == self.turn]
		for piece in pieces:
			if piece.notation == 'k':
				king_pos = piece.pos
		for piece in pieces_atk:
			for square in piece.get_possible_move(self.config , self.squares):
				if square.pos == king_pos:
					output = False
		old_square.piece = changing_piece
		new_square.piece = new_square_old_piece
		changing_piece.pos = old_square.pos
		self.config[x[0]][x[1]] = self.config[y[0]][y[1]]
		self.config[y[0]][y[1]] = temp
		return output

	def checking_end_game(self):
		for square in self.squares:
			if square.piece != None and square.piece.color == self.turn:
				if square.piece.notation == 'k':
					if square.piece.can_castle(self) != []:
						return False
				for sq in square.piece.get_possible_move(self.config , self.squares):
					if self.checkLegalMove(square.pos , sq.pos):
						return False
		return True


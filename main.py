import pygame , sys
from GameEngine import GameState

#global variable
WindowSize = (1240 , 640)
BoardSize = (640 , 640)
SquareSize = (80 , 80)


def menu(display):
	pass

def draw(display , gs , click_piece , click_piece_rect , text , textRect):
	display.fill(pygame.Color(125 , 125 , 125))
	display.blit(text , textRect)
	gs.draw_board(display , click_piece , click_piece_rect)

def main():
	pygame.init()
	screen = pygame.display.set_mode(WindowSize)
	pygame.display.set_caption("Chess")
	clock = pygame.time.Clock()
	screen.fill(pygame.Color(125 , 125 , 125))
	font = pygame.font.Font('freesansbold.ttf', 50)
	menu(screen)


	gs = GameState(BoardSize)
	moving = False
	pos_down = None
	pos_up = None 
	click_piece = None
	click_piece_rect = None
	possible_move = None

	text = "WHITE"
	ending = False
	running = True

	FPS = 60
	clock = pygame.time.Clock()
	# while var_escape == False:

	while running:
		clock.tick(60)
		text = 'WHITE' if gs.turn == 'w' else 'BLACK'
		text = font.render(text , True , (255 , 0 , 0) , (0 , 0 , 255))
		textRect = text.get_rect()
		textRect.center = (140 , 30) if gs.turn == 'w' else (1100 , 30)
		gs.get_king_pos()
		gs.can_check_mate = gs.is_in_check()
		gs.checking_mate()
		ending = gs.checking_end_game()
		if ending and gs.checkmate:
			if gs.turn == 'w':
				print('white lose')
			else:
				print('black lose')
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				running = False

			elif e.type == pygame.MOUSEBUTTONDOWN:
				pos_down = e.pos
				sq = gs.get_square_from_mouse(pos_down)
				if sq != None and sq.piece != None and sq.piece.color == gs.turn:
					possible_move = sq.piece.get_possible_move(gs.config , gs.squares)
					if sq.piece.notation == 'k':
						possible_move += sq.piece.can_castle(gs)
					possible_move = [square for square in possible_move if gs.checkLegalMove(sq.pos , square.pos) is True]
					gs.fill_highlight(possible_move)
					sq.click = True
					click_piece = sq.piece
					click_piece_rect = pygame.Rect(
						e.pos[0],
						e.pos[1],
						80,
						80
					)
					click_piece_rect.center = e.pos
					moving = True
			elif e.type == pygame.MOUSEBUTTONUP and moving:
				pos_up = e.pos
				click_piece = None
				gs.handle_the_click(pos_down , pos_up , possible_move)
				moving = False
			elif e.type == pygame.MOUSEMOTION and moving:
				click_piece_rect.move_ip(e.rel)

		draw(screen , gs , click_piece , click_piece_rect , text , textRect)
		pygame.display.flip()

	pygame.quit()
	sys.exit()

if __name__ == '__main__':
	main()
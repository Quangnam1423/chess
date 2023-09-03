import pygame , sys
from GameEngine import GameState

#global variable
WindowSize = (1240 , 640)
BoardSize = (640 , 640)
SquareSize = (80 , 80)


def menu(display):
	pass

def draw(display , gs , click_piece , click_piece_rect):
	display.fill(pygame.Color(125 , 125 , 125))
	gs.draw_board(display , click_piece , click_piece_rect)

def main():
	pygame.init()
	screen = pygame.display.set_mode(WindowSize)
	pygame.display.set_caption("Chess")
	clock = pygame.time.Clock()
	screen.fill(pygame.Color(125 , 125 , 125))
	menu(screen)
	#start the game 
	gs = GameState(BoardSize)
	moving = False
	pos_down = None
	pos_up = None 
	click_piece = None
	click_piece_rect = None

	running = True

	FPS = 60
	clock = pygame.time.Clock()
	# while var_escape == False:

	while running:
		clock.tick(60)
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				running = False

			elif e.type == pygame.MOUSEBUTTONDOWN:

				pos_down = e.pos
				sq = gs.get_square_from_mouse(pos_down)
				if sq != None:
					click_piece = sq.current_piece
					click_piece_rect = pygame.Rect(
						e.pos[0],
						e.pos[1],
						80,
						80
					)
					click_piece_rect.center = e.pos
					moving = True
			elif e.type == pygame.MOUSEBUTTONUP and moving:
				click_piece = None
				gs.handle_the_click((pos_down[1]//80 , (pos_down[0]-300)//80) , (pos_up[1]//80 , (pos_up[0]-300)//80))
				moving = False
			elif e.type == pygame.MOUSEMOTION and moving:
				pos_up = pygame.mouse.get_pos()
				click_piece_rect.move_ip(e.rel)

		draw(screen , gs , click_piece , click_piece_rect)
		pygame.display.flip()

	pygame.quit()
	sys.exit()

if __name__ == '__main__':
	main()
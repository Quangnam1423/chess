import pygame , sys
from GameEngine import GameState

#global variable
WindowSize = (1240 , 640)
BoardSize = (640 , 640)
SquareSize = (80 , 80)


def menu(display):
	pass

def draw(display , gs):
	gs.draw_board(display)

def main():
	pygame.init()
	screen = pygame.display.set_mode(WindowSize)
	pygame.display.set_caption("Chess")
	clock = pygame.time.Clock()
	screen.fill(pygame.Color(125 , 125 , 125))
	menu(screen)
	#start the game 
	gs = GameState(BoardSize)


	running = True
	while running:
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				running = False
			#elif e.type == MOUSEBUTTONDOWN:
		draw(screen , gs)
		pygame.display.flip()

	pygame.quit()
	sys.exit()

if __name__ == '__main__':
	main()
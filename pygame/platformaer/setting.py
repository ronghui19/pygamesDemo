# game conf settiings
SIZE = WIDTH, HEIGHT = 480, 600
TITLE = 'LETS JUMP'
FPS= 60
FONT_NAME = 'arial'
SPRITESHEET = 'spritesheet_jumper.png'

# player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12

# starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40), 
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
                 (125, HEIGHT - 350, 100, 20),
                 (350, 200, 100, 20),
                 (175, 100, 50, 20)]

# define color
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BGCOLOR = (173, 216, 230)
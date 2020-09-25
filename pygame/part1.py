import pygame,sys
 
size = width, height = 600, 400
fps= 30

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
size = width, height = 600, 400

screen = pygame.display.set_mode(size)
bgcolor = pygame.Color('black')

fclock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    all_sprites.update()

    screen.fill(bgcolor)
    all_sprites.draw(screen)

    pygame.display.update()
    fclock.tick(fps)
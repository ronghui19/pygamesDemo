import pygame,sys
import random
import os

size = width, height = 800, 600
fps= 30

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(img_folder, 'p1_jump.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)
        self.y_speed = 5

    def update(self):
        self.rect.x += 5
        print('#######', self.rect.x)
        self.rect.y += self.y_speed
        if self.rect.bottom > height - 200:
            print(self.rect.bottom)
            self.y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5
        if self.rect.left > width:
            self.rect.right = 0


pygame.init()

screen = pygame.display.set_mode(size)
bgcolor = pygame.Color('black')
fclock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    all_sprites.update()

    screen.fill(bgcolor)
    all_sprites.draw(screen)

    pygame.display.update()
    fclock.tick(fps)
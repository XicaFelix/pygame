import pygame
from random import randint, choice
from GameObject import GameObject
from Apple import Apple
from Strawberry import Strawberry
from Bomb import Bomb
from Player import Player
from Cloud import Cloud

pygame.init()
# Configure the screen
screen = pygame.display.set_mode([500, 500])

all_sprites = pygame.sprite.Group()
fruit_sprites = pygame.sprite.Group()

# Make Clouds
all_sprites.add(Cloud())
all_sprites.add(Cloud())
all_sprites.add(Cloud())
all_sprites.add(Cloud())
all_sprites.add(Cloud())

# Make Fruit instances
apple = Apple()
fruit_sprites.add(apple)
strawberry = Strawberry()
fruit_sprites.add(strawberry)

# make instance of Player
player = Player()

# make bomb
bomb = Bomb()

# Add sprites to group
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(bomb)

clock = pygame.time.Clock()


# Create the game loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      elif event.key == pygame.K_LEFT:
        player.left()
      elif event.key == pygame.K_RIGHT:
        player.right()
      elif event.key == pygame.K_UP:
        player.up()
      elif event.key == pygame.K_DOWN:
        player.down()

  # Clear screen
  screen.fill((26, 36, 99))
  # Move and render Sprites
  for entity in all_sprites:
    entity.move()
    entity.render(screen)
    if entity != player: 
      pass
  # Check Colisions
  fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
  if fruit:
    fruit.reset()

  # Check collision player and bomb
  if pygame.sprite.collide_rect(player, bomb):
    running = False

  pygame.display.flip()

  # tick the clock!
  clock.tick(30)
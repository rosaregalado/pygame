# import modules
import pygame
from random import randint, choice

# import classes
from GameObject import GameObject
from Player import Player
from Apple import Apple
from Strawberry import Strawberry
from Lemon import Lemon
from Banana import Banana
from Bomb import Bomb
from Cloud import Cloud
# from AnimatedBird import AnimatedBird
from ScoreBoard import ScoreBoard



# initialize pygame
pygame.init()
pygame.font.init()

# configure the screen
screen = pygame.display.set_mode([375, 668])
bg = pygame.image.load("images/background-small.png")


# create groups
all_sprites = pygame.sprite.Group()
fruit_sprites = pygame.sprite.Group()

# fruit instances
apple = Apple()
strawberry = Strawberry()
lemon = Lemon()
banana = Banana()

# add fruits to group
fruit_sprites.add(apple)
fruit_sprites.add(strawberry)
fruit_sprites.add(lemon)
fruit_sprites.add(banana)

# instance of Player
player = Player()

# instance of bomb
bomb = Bomb()

# instance of cloud
cloud = Cloud()

# instance of bird
# AnimatedBird = AnimatedBird(10,10,'images/bird')

# instance of score (starting at 0)
score = ScoreBoard(30, 30, 0)

# add sprites to group
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(lemon)
all_sprites.add(banana)
all_sprites.add(bomb)
all_sprites.add(cloud)
# all_sprites.add(AnimatedBird)
all_sprites.add(score)


# Get the clock
clock = pygame.time.Clock()

# ----------------------------------------------
# Create the game loop
running = True
while running:
  # Looks at events
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
  screen.fill((255, 255, 255))
  
  # draw background
  screen.blit(bg, (0, 0))
  

	# Move and render Sprites
  for entity in all_sprites:
    entity.move()
    entity.render(screen)
    if entity != player: 
      pass

	# check for collisions between player and fruits sprites
  fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
  if fruit:
    # update score
    score.update(100)
    fruit.reset()
	
	# Check for collision between player and bomb
  if pygame.sprite.collide_rect(player, bomb):
		# end game
    running = False

  # Update the window
  pygame.display.flip()

  # tick the clock
  clock.tick(30)
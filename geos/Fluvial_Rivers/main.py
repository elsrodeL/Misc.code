import pygame

# init game
pygame.init()

# Window 
HEIGHT, WIDTH = 800, 600
screen = pygame.display.set_mode((HEIGHT,WIDTH))
# Title and Icon 


# Game Loop 
running = True 
while running:
    for event.type in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


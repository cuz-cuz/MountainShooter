import pygame

pygame.init()

window = pygame.display.set_mode(size=(600,480))

while True:dasdas
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # close window
            quit() # end pygame

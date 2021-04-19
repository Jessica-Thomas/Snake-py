import pygame
from pygame.locals import *


# function to draw the block
def draw_block():
    surface.fill((97, 24, 44))
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()

if __name__ == "__main__":
    pygame.init()

    # creating the game window
    surface = pygame.display.set_mode((500, 500))
    # gives a background color using RGB
    surface.fill((97, 24, 44))

    # creating border
    block = pygame.image.load("media/block.jpg").convert()
    block_x = 100
    block_y = 100
    surface.blit(block, (block_x, block_y))


    # Updates the display
    pygame.display.flip()


    running = True

    # event loop integral to any game/program
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # breaks infinite while loop to close game
                if event.key == K_ESCAPE:
                    running = False
                #keystroke actions          
                if event.key == K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()

                         
            # breaks infinite while loop to close game
            elif event.type == QUIT:
                running = False

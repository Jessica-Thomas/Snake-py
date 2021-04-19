import pygame
from pygame.locals import *


class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("media/block.jpg").convert()
        self.x = 100
        self.y = 100

    def draw(self):
        self.parent_screen.fill((97, 24, 44))
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()

    def move_up(self):
        self.y -= 10
        self.draw()

    def move_down(self):
        self.y += 10
        self.draw()

    def move_left(self):
        self.x -= 10
        self.draw()

    def move_right(self):
        self.x += 10
        self.draw()
class Game:
    def __init__(self):
        pygame.init()
        # creating the game window
        self.surface = pygame.display.set_mode((500, 500))
        # gives a background color using RGB
        self.surface.fill((97, 24, 44))
        # creating the snake object within the game class
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self):
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
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()
                            
                # breaks infinite while loop to close game
                elif event.type == QUIT:
                    running = False

if __name__ == "__main__":
    game = Game()
    game.run()

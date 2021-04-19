import pygame
from pygame.locals import *
import time
import random

SIZE = 40


class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("media/apple.jpg").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()     
    
    def move(self):
        self.x = random.randint(1,25)*SIZE
        self.y = random.randint(1,20)*SIZE
class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("media/block.png").convert()
        self.direction = 'right'     

        self.length = length
        self.x = [SIZE] * length
        self.y = [SIZE] * length

    # changes direction based on keystroke
    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    # makes block move until we hit another key to change direction
    def walk(self):
        # updates body block positions
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # updated head position
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        
        self.draw()
    
    def draw(self):
        self.parent_screen.fill((97, 24, 44))

        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()
    
    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
class Game:
    def __init__(self):
        pygame.init()
        # creating the game window
        self.surface = pygame.display.set_mode((800, 800))
        # creating the snake object within the game class
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def play(self):
        self.snake.walk()
        self.apple.draw()

    def run(self):
        running = True

        # event loop integral to any game/program
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # breaks infinite while loop to close game by pressing escape key
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
                            
                # breaks infinite while loop to close game by clicking X
                elif event.type == QUIT:
                    running = False

            self.play()
            
            time.sleep(0.2)


# main funtion that pulls everything together and executes game
if __name__ == "__main__":
    game = Game()
    game.run()

import pygame
from pygame.locals import *
import time
import random

#apple and block are 40x40 px
SIZE = 40
FONT_COLOR = (255,255,255)

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
        self.x = random.randint(1,19)*SIZE
        self.y = random.randint(1,19)*SIZE
class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("media/block.png").convert()
        self.direction = 'right'     

        self.length = 1
        self.x = [SIZE] 
        self.y = [SIZE]

    # changes direction based on keystroke
    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

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
        pygame.display.set_caption("It's a snaaaaake")

        pygame.mixer.init()
        # self.background_music()

        # creating the game window
        self.surface = pygame.display.set_mode((800, 800))
        # creating the snake object within the game class
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    # def background_music(self):
    #     pygame.mixer.music.load("media/bg_music_1.mp3")
    #     pygame.mixer.music.play(-1, 0)

    # def play_sound(self, sound_name):
    #     if sound_name == "crash":
    #         sound = pygame.mixer.Sound("media/crash.mp3")
    #     elif sound_name == 'ding':
    #         sound = pygame.mixer.Sound("media/ding.mp3")

    #     pygame.mixer.Sound.play(sound)

    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)

    # collision logic, add block to snake when snake collides with/eats apple
    def collision(self, x1, y1, x2 ,y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def display_background(self):
        bg = pygame.image.load("media/background.png")
        self.surface.blit(bg, (0,0))

    def show_score(self):
        font = pygame.font.SysFont('arial',30, bold=True)
        score = font.render(f"Score: {self.snake.length-1}",True,FONT_COLOR)
        self.surface.blit(score,(600,10))

    def play(self):
        self.display_background()
        self.snake.walk()
        self.apple.draw()
        self.show_score()
        pygame.display.flip()

        # checks if the head of the snake [0] has collided with the apple.... if  true, adds another block to the body.
        if self.collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            # self.play_sound("ding")
            self.snake.increase_length()
            self.apple.move()

        # logic for snake colliding with itself
        for i in range(3, self.snake.length):
            if self.collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                # self.play_sound('crash')
                raise "Game Over, suckkaaaa"

        # snake colliding with the boundries of the window
        if not (0 <= self.snake.x[0] <= 800 and 0 <= self.snake.y[0] <= 800):
            # self.play_sound('crash')
            raise "You hit the side, bro. Game over."

    def game_over(self):
        self.display_background()
        font = pygame.font.SysFont('arial',25, bold=True)
        line1 = font.render(f"GAME OVER. Your score is {self.snake.length-1}",True,FONT_COLOR)   
        self.surface.blit(line1, (100,300))     
        line2 = font.render("Want to play again? Press Y. To exit, press Escape.", True, FONT_COLOR)
        self.surface.blit(line2, (100,350))     
        pygame.display.flip()

        # pygame.mixer.music.pause()

    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)

    def run(self):
        running = True
        pause = False

        # event loop integral to any game/program
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:

                    # breaks infinite while loop to close game by pressing escape key
                    if event.key == K_ESCAPE:
                        running = False
                  
                    if event.key == K_y:
                        pygame.mixer.music.unpause()
                        pause = False

                    #don't process other keystrokes if game is paused
                    if not pause:
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
            try:
                if not pause:
                    self.play()
            
            except Exception as e:
                self.game_over()
                pause = True
                self.reset() 

            time.sleep(0.25)


# main funtion that pulls everything together and executes game
if __name__ == "__main__":
    game = Game()
    game.run()

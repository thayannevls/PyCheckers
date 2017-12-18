import pygame, sys
from graphics import Graphics
from board import Board
from pygame.locals import *


class Game:
    def __init__(self):
        self.graphics = Graphics()
        self.board = Board()
		
    def setup(self):
        self.graphics.setup_window()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit()

    def update(self):
        self.graphics.update(self.board)
    
    def quit(self):
        pygame.quit()
        sys.exit()
    
    def main(self):
        self.setup()

        while True:
            self.event_loop()
            self.update()

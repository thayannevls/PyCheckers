import pygame, sys
from pygame.locals import *

from graphics import Graphics
from board import Board
from resources import BLUE, RED


class Game:
    def __init__(self):
        self.graphics = Graphics()
        self.board = Board()
        self.selected_piece = None  

    def setup(self):
        self.graphics.setup_window()

    def event_loop(self):
        self.mouse_pos = self.graphics.board_coords(pygame.mouse.get_pos())

        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit()
            if event.type == MOUSEBUTTONDOWN:
                if self.board.location(self.mouse_pos).occupant != None and \
                    self.board.location(self.mouse_pos).occupant.color == self.turn:
						self.selected_piece = self.mouse_pos

                elif self.selected_piece != None and self.mouse_pos in \
                    self.board.legal_moves(self.selected_piece):
                    self.board.move_piece(self.selected_piece, self.mouse_pos)
                
                else:
                    self.end_turn()
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

    def end_turn(self):
        if self.turn == BLUE:   
            self.turn = RED
        else:
            self.turn = BLUE


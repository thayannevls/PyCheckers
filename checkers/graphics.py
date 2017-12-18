from resources import GOLD, HIGH
import pygame
from pygame.locals import *


class Graphics:
    def __init__(self):
        self.window_size = 600
        self.background = pygame.image.load('checkers/resources/board.png')
        self.screen = pygame.display.set_mode((self.window_size, self.window_size))
        self.square_size = self.window_size / 8
        self.piece_size = self.square_size / 2
    
    def setup_window(self):
        pygame.init()
    
    def update(self, board):
        self.screen.blit(self.background, (0,0))
        self.draw_board_pieces(board)
        pygame.display.update()
    
    def draw_board_squares(self, board):
        for i in range(8):
            for j in range(8):
                pygame.draw.rect(self.screen, board[i][j].color, (i * self.square_size, j * self.square_size, self.square_size, self.square_size), )

    def draw_board_pieces(self, board):
		for x in xrange(8):
			for y in xrange(8):
				if board.matrix[x][y].occupant != None:
					pygame.draw.circle(self.screen, board.matrix[x][y].occupant.color, self.pixel_coords((x,y)), self.piece_size) 

    def pixel_coords(self, board_coords):
		
		return (board_coords[0] * self.square_size + self.piece_size, board_coords[1] * self.square_size + self.piece_size)

    def board_coords(self, (pixel_x, pixel_y)):
        return (pixel_x / self.square_size, pixel_y / self.square_size)	

	def highlight_squares(self, squares, origin):
		for square in squares:
			pygame.draw.rect(self.screen, HIGH, (square[0] * self.square_size, square[1] * self.square_size, self.square_size, self.square_size))	

		if origin != None:
			pygame.draw.rect(self.screen, HIGH, (origin[0] * self.square_size, origin[1] *  self.square_size, self.square_size, self.square_size))
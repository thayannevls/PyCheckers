from resources.color import WHITE, BLACK, RED, BLUE
from resources import NORTHEAST, NORTHWEST, SOUTHEAST, SOUTHWEST


class Board:
    def __init__(self):
        self.matrix = self.new_board()

    def new_board(self):
        matrix = [[None] * 8 for i in range(8)]

        for i in range(8):
            for j in range(8):
                if (i % 2 != 0) and (j % 2 == 0):
					matrix[j][i] = Square(WHITE)
                elif (i % 2 != 0) and (j % 2 != 0):
					matrix[j][i] = Square(BLACK)
                elif (i % 2 == 0) and (j % 2 != 0):
					matrix[j][i] = Square(WHITE)
                elif (i % 2 == 0) and (j % 2 == 0): 
					matrix[j][i] = Square(BLACK)
        
        for x in xrange(8):
			for y in xrange(3):
				if matrix[x][y].color == BLACK:
					matrix[x][y].occupant = Piece(RED)
			for y in xrange(5, 8):
				if matrix[x][y].color == BLACK:
					matrix[x][y].occupant = Piece(BLUE)
        return matrix

    def remove_piece(self, (x,y)):
        self.matrix[x][y].occupant = None

    def move_piece(self, (start_x, start_y), (end_x, end_y)):
        self.matrix[end_x][end_y].occupant = self.matrix[start_x][start_y].occupant
        self.remove_piece((start_x, start_y))
    
    def on_board(self, (x,y)):
        if x < 0 or y < 0 or x > 7 or y > 7:
            return False

        return True

    def location(self, (x,y)):
        return self.matrix[x][y]
    
    def adjacents_coordinates(self, (x,y), direction=None):
        if direction == NORTHWEST:
            return (x - 1, y + 1)
        if direction == NORTHEAST:
            return (x + 1, y + 1)
        if direction == SOUTHWEST:
			return (x - 1, y - 1)
        if direction == SOUTHEAST:
			return (x + 1, y - 1)
        
        return [(x - 1, y + 1), (x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1)]

    def moves(self, (x,y)):

        if self.matrix[x][y].occupant.king == True:
            return self.adjacents_coordinates((x,y))
        if self.matrix[x][y].occupant.color == BLUE:
			return [self.adjacents_coordinates(NORTHWEST, (x,y)), self.adjacents_coordinates(NORTHEAST, (x,y))]
        if self.matrix[x][y].occupant.color == RED:
            return [self.adjacents_coordinates(SOUTHWEST, (x,y)), self.adjacents_coordinates(SOUTHEAST, (x,y))]

    def legal_moves(self, (x,y)):
        moves = self.moves((x,y))
        legal_moves = []

        for move in moves:
            if self.on_board(move):
                if self.location(move).occupant = None:
                    legal_moves.append(move)
                elif self.location(move).occupant.color != self.matrix[x][y].occupant.color and self.on_board((move[0] + (move[0] - x), move[1] + (move[1] - y))) and 
                    self.location((move[0] + (move[0] - x), move[1] + (move[1] - y))).occupant == None:
                    legal_moves.append((move[0] + (move[0] - x), move[1] + (move[1] - y)))


class Square:
    def __init__(self, color, occupant = None):
        self.color = color
        self.occupant = occupant


class Piece:
	def __init__(self, color):
		self.color = color
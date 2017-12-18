from resources.color import WHITE, BLACK, RED, BLUE

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


class Square:
    def __init__(self, color, occupant = None):
        self.color = color
        self.occupant = occupant


class Piece:
	def __init__(self, color, king = False):
		self.color = color
		self.king = king
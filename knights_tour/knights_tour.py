'''
Created on Oct 30, 2012

@author: Joe Lee
'''
from random import randint
from tile import Tile

class KnightsTour(object):
    '''
    classdocs
    '''
    _leftSquare = {(2,0),(0,1),(1,3),(3,2),
                  (6,0),(4,1),(5,3),(7,2),
                  (6,4),(4,5),(7,6),(5,7),
                  (2,4),(0,5),(3,6),(1,7)}
    _rightSquare = {(1,0),(0,2),(3,1),(2,3),
                    (5,0),(4,2),(7,1),(6,3),
                    (5,4),(7,5),(6,7),(4,6),
                    (1,4),(3,5),(0,6),(2,7)}
    _leftDiamond = {(0,0),(2,1),(1,2),(3,3),
                    (4,0),(6,1),(5,2),(7,3),
                    (4,4),(6,5),(5,6),(7,7),
                    (0,4),(2,5),(1,6),(3,7)}
    _rightDiamond = {(3,0),(0,3),(1,1),(2,2),
                     (7,0),(5,1),(6,2),(4,3),
                     (7,4),(5,5),(6,6),(4,7),
                     (3,4),(1,5),(2,6),(0,7)}
    
    q1, q2, q3, q4 = range(1, 5)
    
    def __init__(selfparams):
        '''
        Constructor
        '''
    
    def solve(self):
        self._board = self._create_board()
        self._length = len(self._board)
        solved = 0
        moves = []
        moves.append(self._start)
        self._board[self._start.get_row()][self._start.get_col()] = "X"
        
        while solved < 4:
            current = moves[len(moves) - 1]
            if (current.get_row(), current.get_col()) in self._leftSquare:
                self._solve_pattern(moves, self._leftSquare)
                solved += 1
            elif (current.get_row(), current.get_col()) in self._rightSquare:
                self._solve_pattern(moves, self._rightSquare)
                solved += 1
            elif (current.get_row(), current.get_col()) in self._leftDiamond:
                self._solve_pattern(moves, self._leftDiamond)
                solved += 1
            elif (current.get_row(), current.get_col()) in self._rightDiamond:
                self._solve_pattern(moves, self._rightDiamond)
                solved += 1
        self._display_moves(moves)
        self._display_board()
        
    def _solve_pattern(self, moves, pattern):
        current = moves[len(moves) - 1]
        count = 0
        rewind = 0
        
        while count < 16:
            quad = self._get_quad(current.get_row(), current.get_col())
            quadCount = 0
            
            while quadCount < 3:
                next = self._get_move(moves)
                
                if (next.get_row(), next.get_col()) in pattern and quad == self._get_quad(next.get_row(), next.get_col()):
                    moves.append(next)
                    self._board[next.get_row()][next.get_col()] = next.get_count()
                    
                    if next.get_count() == 63:
                        return
                    
                    count += 1
                    quadCount += 1

                    
            #switch patterns if pattern is complete
            if count % 15 == 0:
                while True:
                    next = self._get_move(moves)
                    if next.get_move() == -1:
                        self._rewind(moves)
                        count -= 3
                        break
                    if quad != self._get_quad(next.get_row(), next.get_col()):
                        moves.append(next)
                        self._board[next.get_row()][next.get_col()] = next.get_count()
                        count += 1
                        return
                continue
                           
            while True: #switch quadrants
                next = self._get_move(moves)
                if (next.get_row(), next.get_col()) in pattern and quad != self._get_quad(next.get_row(), next.get_col()):
                    moves.append(next)
                    self._board[next.get_row()][next.get_col()] = next.get_count()
                    count += 1
                    current = next
                    break
                
                #rewind if unable to switch quadrants
                if next.get_move() == -1:
                    self._rewind(moves)
                    count -= 3
                    break
                
    def _rewind(self, moves):
        for i in range(3):
            remove = moves.pop()
            self._board[remove.get_row()][remove.get_col()] = 0


    
    def _create_board(self):
            board = [
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0]
             ]
            row = randint(0, 7)
            col = randint(0, 7)
            self._start = Tile(row, col, 0, 0)
            return board
    
    def _display_board(self):
        print()
        print("---Board Numbered By Moves (\"X\" is the starting point)---")
        for row in range(self._length):
            print()
            if row == 0:
                print(" ____ ____ ____ ____ ____ ____ ____ ____")
            else:
                print("|____|____|____|____|____|____|____|____|")
            for col in range(self._length):
                if col == self._length -1:
                    if self._board[row][col]:
                        print(str.format("| {0:2} |", self._board[row][col]),  end="")
                    else:
                        print("|    |", end="")
                else:
                    if self._board[row][col]:
                        print(str.format("| {0:2} ", self._board[row][col]), end="")
                    else:
                        print("|    ", end="")
        print()
        print("|____|____|____|____|____|____|____|____|")
        
    def _get_quad(self, row, col):
        if row >= 0 and row <= 3:
            if col >= 0 and col <= 3:
                return self.q1            
        if row >= 4 and row <= 7:
            if col >= 0 and col <= 3:
                return self.q2            
        if row >= 4 and row <= 7:
            if col >= 4 and col <= 7:
                return self.q3    
        return self.q4
        
    def _get_move(self, moves):
        prev = moves[len(moves) - 1]
        move = prev.get_move()
        row = prev.get_row()
        col = prev.get_col()
        while True:
            move += 1
            if move == 1:
                if self._legal(row - 2, col - 1) == 0:
                    moves.pop()
                    moves.append(Tile(row, col, 1, prev.get_count()))
                    tile = Tile(row - 2, col - 1, 0, prev.get_count() + 1)
                    #moves.append(((row, col), 1, prev[2]))
                    return(tile)
            elif move == 2:
                if self._legal(row - 1, col - 2) == 0:
                    moves.pop()
                    moves.append(Tile(row, col, 2, prev.get_count()))
                    tile = Tile(row - 1, col - 2, 0, prev.get_count() + 1)
                    return(tile)
            elif move == 3:
                if self._legal(row + 1, col - 2) == 0:
                    moves.pop()
                    moves.append(Tile(row, col, 3, prev.get_count()))
                    tile = Tile(row + 1, col - 2, 0, prev.get_count() + 1)
                    return(tile)
            elif move == 4:
                if self._legal(row + 2, col - 1) == 0:
                    moves.pop()
                    moves.append(Tile(row, col, 4, prev.get_count()))
                    tile = Tile(row + 2, col - 1, 0, prev.get_count() + 1)
                    return(tile)
            elif move == 5:
                if self._legal(row + 2, col + 1) == 0:
                    moves.pop()
                    moves.append(Tile(row, col, 5, prev.get_count()))
                    tile = Tile(row + 2, col + 1, 0, prev.get_count() + 1)
                    return(tile)
            elif move == 6:
                if self._legal(row + 1, col + 2) == 0:
                    moves.pop()
                    moves.append(Tile(row, col, 6, prev.get_count()))
                    tile = Tile(row + 1, col + 2, 0, prev.get_count() + 1)
                    return(tile)
            elif move == 7:
                if self._legal(row - 1, col + 2) == 0:
                    moves.pop()
                    moves.append(Tile(row, col, 7, prev.get_count()))
                    tile = Tile(row - 1, col + 2, 0, prev.get_count() + 1)
                    return(tile) 
            elif move == 8:
                if self._legal(row - 2, col + 1) == 0:
                    moves.pop()
                    moves.append(Tile(row, col, 8, prev.get_count()))
                    tile = Tile(row - 2, col + 1, 0, prev.get_count() + 1)
                    return(tile)
            else:
                return (Tile(-1, -1, -1, -1))
        
    def _legal(self, row, col):
        if row < 0 or row >= self._length:
            return 1
        elif col < 0 or col >= self._length:
            return 1
        elif self._board[row][col] != 0:
            return 1
        else:
            return 0

    def _display_moves(self, moves):
        print("---Moves from start to finish---")
        for i in range(len(moves)):
            move = moves[i]
            print(move, end = "")
            if i % 8 == 7:
                print()
        
        
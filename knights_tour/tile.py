'''
Created on Nov 4, 2012

@author: Joe Lee
'''

class Tile(object):
    '''
    classdocs
    '''


    def __init__(self, row, col, move, count):
        '''
        Constructor
        '''
        self._move = move
        self._count = count
        self._set_row(row)
        self._set_col(col)
        
    
    def _set_row(self, r):
        self._row = r
    
    def _set_col(self, c):
        self._col = c
    
    def get_row(self):
        return self._row
    
    def get_col(self):
        return self._col
    
    def get_move(self):
        return self._move
    
    def get_count(self):
        return self._count
    
    def __str__(self):
        return str.format("{0:2}. ({1}, {2}) ", self._count, self._row, self._col)
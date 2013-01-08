'''
Created on Oct 30, 2012

@author: Joe Lee
'''
from knights_tour import KnightsTour
from tile import Tile

def main():

    tour = KnightsTour()
    tour.solve()
    
    input("\npress any key to end")
    




if __name__ == '__main__':
    main()
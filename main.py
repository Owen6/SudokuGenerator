import random


class Board:

    fillCount = 0

    def __init__(self, initial_board = None):
         self.board = initial_board if initial_board is not None else [[0]*9 for _ in range(9)]

    def displayBoard(self):
         for row in self.board:
              print(" ".join(str(num) if num != 0 else '.' for num in row))

    def validMove(self, row, col, number):
         #Check row
         if number in self.board[row]:
              return False
         #Check col
         for i in range(9):
              if self.board[i][col] == number:
                   return False
         #Check 3x3 box
         startRow = 3 * (row // 3)
         startCol = 3 * (col // 3)
         for i in range(3):
              for j in range(3):
                   if self.board[startRow+i][startCol+j] == number:
                        return False
         return True
    
    def isEmpty(self, row, col):
         return self.board[row][col] == 0
         
    def setValue(self, row, col, number):
         if self.validMove(row, col, number):
              self.board[row][col] = number
         else:
              print("Invalid move")

    def splitList(self, list, depth = 1):
        permutations = []
        permutations.append(list)
        if depth > 3:
             return list
        else:
            self.splitList(list[-3:] + list[:-3], depth + 1)
        for i in range(9):
             self.board[depth-1+self.fillCount][i] = permutations[0][i]

    def CreatePuzzle(self):
        #Generate a list of the numbers 1 to 9 in a random order
        temp = list(range(1,10))
        random.shuffle(temp)

        #Shuffle the list of numbers 1 to 9 by shifting the col by one and finding all permutations of 3 in the list
        for i in range(3):
          self.splitList(temp)
          self.fillCount = self.fillCount + 3
          temp = temp[-1:] + temp[:-1]
    
    def flipRowCol(self):
         self.board = [[self.board[j][i] for j in range(len(self.board))] for i in range(len(self.board[0]))]

    def shuffleBoard(self, val = 0):
         #Shuffle rows of board
         shuffleSet1 = self.board[0:3].copy()
         random.shuffle(shuffleSet1)
         shuffleSet2 = self.board[3:6].copy()
         random.shuffle(shuffleSet2)
         shuffleSet3 = self.board[6:9].copy()
         random.shuffle(shuffleSet3)

         self.board = shuffleSet1 + shuffleSet2 + shuffleSet3

         #Shuffle columns of board
         if val == 0:
              self.flipRowCol()
              self.shuffleBoard(1)
        

def main():
     board = Board()
     board.CreatePuzzle()
     board.displayBoard()
     board.shuffleBoard()
     print(' ')
     board.displayBoard()

if __name__ == "__main__":
     main()
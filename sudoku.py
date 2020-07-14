import copy

class Sudoku():
    def __init__(self,board):
        self.board = board
        self.end = 0 #stop after 1 solution for solveOne
        self.solutions = [] #store solutions for solveAll
    
    def printBoard(self):
        for i in range (0,9):
            for j in range (0,9):
                print(self.board[i][j],end=' ')
            print('\n',end='')
        print('\n',end='')
    
    #check if the puzzle is complete
    def checkDone(self):
        for i in range (0,9):
            for j in range (0,9):
                if self.board[i][j] == 0:
                    return False
        return True

    #check used values in the 3x3 and in the line&column
    def checkOptions(self,i,j):
        offset = [x for x in range (0,3)]
        h_offset = [((x+i)%3 - i%3) for x in offset]
        v_offset = [((x+j)%3 - j%3) for x in offset]
        used_val = []
        #check 3x3 square for used values
        for ii in h_offset:
            for jj in v_offset:
                used_val.append(self.board[i+ii][j+jj])
        line_offset = [x for x in range (0,9)]
        h_line_offset = [((x+i)%9 - i%9) for x in line_offset]
        v_line_offset = [((x+j)%9 - j%9) for x in line_offset]
        #check line
        for ii in h_line_offset:
            used_val.append(self.board[i+ii][j])
        #check column
        for jj in v_line_offset:
            used_val.append(self.board[i][j+jj])
        used_val = list(set(used_val))
        return used_val
    
    #add a deep copy of a solved board to list of solutions
    def addSolution(self):
        sol = copy.deepcopy(self.board)
        self.solutions.append(sol)

    def solveOne(self):
        if self.checkDone():
            print('********DONE*********')
            self.printBoard()
            print('********DONE*********')
            self.end = 1
            return
        
        if self.end == 0:
            for i in range (0,9):
                for j in range (0,9):
                    if self.board[i][j] == 0:
                        #check used values
                        used = self.checkOptions(i,j)
                        #determine remaining options
                        remaining = [x for x in range(1,10) if x not in used]
                        if (len(remaining)>0):
                            #iterate through the remaining options
                            for val in remaining:
                                self.board[i][j] = val
                                self.solveOne()
                                #set value to zero upon return from recursion
                                self.board[i][j] = 0
                        return

    #solves for all solutions to the puzzle
    def solver(self):
        if self.checkDone():
            self.addSolution()
            return
        
        for i in range (0,9):
            for j in range (0,9):
                if self.board[i][j] == 0:
                    used = self.checkOptions(i,j)
                    remaining = [x for x in range(1,10) if x not in used]
                    if (len(remaining)>0):
                        for val in remaining:
                            self.board[i][j] = val
                            self.solver()
                            self.board[i][j] = 0
                    return
    
    def solveAll(self):
        #call solver to get all solutions
        self.solver()
        print(len(self.solutions),'solutions found.')
        for sol in self.solutions:
            for i in range (0,9):
                for j in range (0,9):
                    print(sol[i][j],end=' ')
                print('\n',end='')
            print('\n',end='')


board = [[9,2,0,0,0,0,7,0,0],
         [0,0,0,0,0,2,4,3,9],
         [0,0,0,0,1,0,5,0,0],
         [0,0,0,0,0,5,0,0,0],
         [0,4,0,0,7,8,1,0,0],
         [0,6,8,0,3,0,2,0,0],
         [6,0,5,0,0,0,3,0,0],
         [7,3,4,1,2,0,0,0,8],
         [2,0,0,0,0,0,0,7,0]]

game = Sudoku(board)
game.printBoard()
game.solveAll()
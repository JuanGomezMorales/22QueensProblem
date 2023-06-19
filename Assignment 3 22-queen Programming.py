# ## Assignment 3, 22-Queen Programming

# Your homework must be implemented in this Notebook file. 
# You can add as many cells as you want. However, you are not allowed to touch the code below the line "=============".
# 

# In[4]:


#n is the number of queens
n=10

#class to store info about each square (node) on the chess board
class Chess_Node:
    row = 0;
    column = 0;
    #queen is a boolean to mark if a queen is there or not
    queen = False;
    def __init__(self, row, column, queen):
        self.row = row
        self.column = column
        self.queen = queen
    def getRow(self):
        return self.row
    def getColumn(self):
        return self.column
    def getQueen(self):
        return self.queen
    def setRow(self, row):
        self.row = row
    def setColumn(self, column):
        self.column = column
    def setQueen(self, queen):
        self.queen = queen
    #Algorithm to check if the current node could be attacked by a queen on another node
    def attackable(self, node):
        if self.row == node.getRow():
            return True
        if self.column == node.getColumn():
            return True
        if abs(self.row - node.getRow()) == abs(self.column - node.getColumn()):
            return True
        return False
    def __str__(self):
        return "(" + str(self.row) + "," + str(self.column) + ")"

#function to check if a queen could be attacked by another
def amIAttackable(chessBoard, queen):
    #check entire board to see if any nodes are attackable
    for i in range(len(chessBoard)):
        if queen.attackable(chessBoard[i]):
            return True
    return False

#Recursive function that goes through the board and finds solutions
def recursive_backtracing(index, csp, solution):
    if len(solution) == n:
        return solution
    ind = index
    while ind < len(csp):
        csp[ind].setQueen(True)
        if amIAttackable(solution, csp[ind]) == False:
            solution += [csp[ind]]
            result = recursive_backtracing(index + 1, csp, solution)
            if result[0].getRow() != -1:
                return result
            else:
                solution.pop()
        csp[ind].setQueen(False)
        ind += 1
    return [Chess_Node(-1, -1, False)]

#print the solution as (row, column) pairs
def print_result(result):
    for i in range(len(result)):
        for j in range(len(result[i])):
            print(str(result[i][j]), end='')
        print("\n")

#define csp to store the chess board
csp = []
for i in range(n):
    for j in range(n):
        csp += [Chess_Node(i, j, False)]
#define result to store answer
result = []
for i in range(4):
    result += [recursive_backtracing(i, csp, [])]
print_result(result)
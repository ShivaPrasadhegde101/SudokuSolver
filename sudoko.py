board=[]
print("Enter 0 for Blank")
print("Enter your numbers(9X9):")
for i in range(9):
        a = []
        for j in range(9):
            a.append(int(input()))
        board.append(a)


def print_board(b):
    for i in range(len(b)):
        if i %3==0 and i!=0:
            print("------------------------------")
        for j in range(len(b[0])):
            if j % 3==0 and j!=0:
                print("|",end=" ")

            if j==8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ",end=" ")


def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j]==0:
                return (i,j)
    return False


def valid(b,num,pos):
    for i in range(len(b[0])):
        if b[pos[0]][i]==num and pos[1]!=i:   #row check
            return False
    for i in range(len(b[0])):
        if b[i][pos[1]]==num and pos[0]!=i:   #column Check
            return False
    box_x=pos[1]//3
    box_y=pos[0]//3
    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if b[i][j]==num and (i,j)!=pos:
                return False
    return True


def solve(b):
    f=find_empty(b)
    if not f:
        return True
    else:
        row,col=f
    for i in range(1,10):
        if valid(b,i,(row,col)):
            b[row][col]=i

            if solve(b):
                return True
            b[row][col]=0
    return False

print("Your Board Before Solving")
print_board(board)
print()
print()
print("Your Solution:")
solve(board)
print_board(board)

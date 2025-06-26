board = """\
    ....
    K...
    ..R.
    ....\
    """
    
lst = board.split()
# print(lst)
def checkmate(lst):
    size = len(lst)
    for row in range(0, len(lst)):
        for col in range(0, len(lst)):    
            if lst[row][col] == 'P':
                pawn_attack(lst,row,col,size)
            elif lst[row][col] == 'R':
                print('R')
            elif lst[row][col] == 'B':
                print('B')
                
def pawn_attack(board,row,col,size):
    if board[row-1][col-1] == 'K':
        # print(row,col )
        print(size)
        print("Success")
    elif board[row-1][col+1] == 'K':
        print("Success")
    else:
        print(size)
        # print(board[row][col])
        print('Fail')
    
                
checkmate(lst)

    
    
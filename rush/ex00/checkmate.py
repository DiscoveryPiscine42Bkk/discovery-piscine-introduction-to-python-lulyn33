board = """\
    .... 
    ....
    .K.K
    ..B.\
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
                rook_attack(lst,row,col,size)
            elif lst[row][col] == 'B':
                bishop_attack(lst,row,col,size)
                
def pawn_attack(board,row,col,size):
    try:
        col < size
        if board[row-1][col-1] == 'K':
            print("Success")
        elif board[row-1][col+1] == 'K':
            print("Success")
        else:
            print('Fail')
            
    except IndexError:
        print('Fail')
#pawn attack is done        

def rook_attack(board,row,col,size):
    found = False
    for c in range(size):
        if board[row][c] == 'K':
            # print(board[row][c],end=' ')
            print('Success')
            found = True
            break
    
    for r in range(size):
        if board[r][col] == 'K':
            print('Success')           
            found = True
            break
        
    if not found:
        print('Fail')    
#rook attack is done

def bishop_attack(board,row,col,size):
    for r in range(size):
        for c in range(size):
            if board[row-r][col-c] == 'K':
                print('Success')
            elif c < size+1:
                if board[row-r][col+c] == 'K':
                    print('Success')
            
    
checkmate(lst)

    
    
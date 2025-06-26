board = """\
..
.K\
"""
    
lst = board.split()
# print(lst)
def checkmate(lst):
    size = len(lst)
    for row in range(0, len(lst)):
        for col in range(0, len(lst)):
            if not lst[row][col] in ['P',"Q","B","R"]:
                success = False #give one variable as success = False
            else:       
                if lst[row][col] == 'P':
                    pawn_attack(lst,row,col,size)
                elif lst[row][col] == 'R':
                    rook_attack(lst,row,col,size)
                elif lst[row][col] == 'B':
                    bishop_attack(lst,row,col,size)
                elif lst[row][col] == 'Q':
                    queen_attack(lst,row,col,size)
            
                
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
            found = True
            break
    
    for r in range(size):
        if board[r][col] == 'K':      
            found = True
            break
        
    print("Success" if found else "Fail")  
#rook attack is done

def bishop_attack(board,row,col,size):
    found = False
    
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        if board[r][c] == 'K':
            found = True
            break
        r -= 1
        c -= 1

    r, c = row - 1, col + 1
    while r >= 0 and c < size:
        if board[r][c] == 'K':
            found = True
            break
        r -= 1
        c += 1

    r, c = row + 1, col - 1
    while r < size and c >= 0:
        if board[r][c] == 'K':
            found = True
            break
        r += 1
        c -= 1

    r, c = row + 1, col + 1
    while r < size and c < size:
        if board[r][c] == 'K':
            found = True
            break
        r += 1
        c += 1

    print("Success" if found else "Fail")
 
def queen_attack(board,row,col,size):
    found = False
    for i in range(size):
            if board[i][col] == 'K' or board[row][i] == 'K':
                found = True
            else:
                continue
                
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        if board[r][c] == 'K':
            found = True
            break
        r -= 1
        c -= 1

    r, c = row - 1, col + 1
    while r >= 0 and c < size:
        if board[r][c] == 'K':
            found = True
            break
        r -= 1
        c += 1

    r, c = row + 1, col - 1
    while r < size and c >= 0:
        if board[r][c] == 'K':
            found = True
            break
        r += 1
        c -= 1

    r, c = row + 1, col + 1
    while r < size and c < size:
        if board[r][c] == 'K':
            found = True
            break
        r += 1
        c += 1
        
    print("Success" if found else "Fail")

checkmate(lst)

    
    
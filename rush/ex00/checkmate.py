def checkmate(board):
    lst = board.split()

    size = len(lst)
    for row in range(0, len(lst)):
        for col in range(0, len(lst)):
            if lst[row][col] == 'P' and pawn_attack(lst,row,col,size) == "Success":
                return "Success"
            elif lst[row][col] == 'R' and rook_attack(lst,row,col,size) == "Success":
                return "Success"
            elif lst[row][col] == 'B' and bishop_attack(lst,row,col,size) == "Success":
                return "Success"
            elif lst[row][col] == 'Q' and queen_attack(lst,row,col,size) == "Success":
                return "Success"
                            
    return "Fail"      
                
def pawn_attack(board,row,col,size):
    try:
        col < size
        if board[row-1][col-1] == 'K':
            return "Success"
        elif board[row-1][col+1] == 'K':
            return "Success"
        else:
            return "Fail"
            
    except IndexError:
        return "Fail"
#pawn attack is done        

def rook_attack(board,row,col,size):
    r = row - 1
    while r >= 0:
        if board[r][col] == 'K':
           return 'Success'
        elif board[r][col] != '.':
            break
        r -= 1
    
    r = row+1
    while r < size:
        if board[r][col] == 'K':
            return 'Success'
        elif board[r][col] != '.':
            break
        r += 1
    
    c = col -1
    while c >= 0:
        if board[row][c] == 'K':
            return 'Success'
        elif board[row][c] != '.':
            break
        c -= 1 
            
    c = col + 1
    while c < size:
        if board[row][c] == 'K':
            return 'Success'
        elif board[row][c] != '.':
            break
        c +=1
        
    return "Fail"
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

    return "Success" if found else "Fail"
 
def queen_attack(board,row,col,size):
    if rook_attack(board,row,col,size) == "Success" or bishop_attack(board,row,col,size) == 'Success':
        return 'Success'
    else:
        return 'Fail'

def checkmate(board):
    lst = board.split() 

    size = len(lst)
    for i in lst:
        if len(i) != size:
            print('Fail')
            square = False
            break
        else:
            square = True
    
    check_k_lst = []
    for k in lst:
        for l in range(len(lst)):
            if k[l] == 'K':
                check_k_lst.append(k[l])
    
    if len(check_k_lst) > 1:
        print('Fail')
        square = False
    else:
        square = True
            
    found = False
    while square:
        for row in range(0, len(lst)):
            for col in range(0, len(lst)):

                if lst[row][col] == 'P' and pawn_attack(lst,row,col,size) == "Success":
                    found = True
                    
                elif lst[row][col] == 'R' and rook_attack(lst,row,col,size) == "Success":
                    found = True
                    
                elif lst[row][col] == 'B' and bishop_attack(lst,row,col,size) == "Success":
                    found = True
                    
                elif lst[row][col] == 'Q' and queen_attack(lst,row,col,size) == "Success":
                    found = True
                    
        if found:
            print('Success')
        else:
            print('Fail')
        break
                     
                
def pawn_attack(board,row,col,size):
    
    if row - 1 >= 0:
        if col - 1 >= 0 and board[row - 1][col - 1] == 'K':
            return "Success"
        if col + 1 < size and board[row - 1][col + 1] == 'K':
            return "Success"
    return "Fail"     
#pawn attack       

def rook_attack(board,row,col,size):
    r = row - 1
    while r >= 0:
        if board[r][col] == 'K':
           return("Success")
        elif board[r][col] != '.':
            break
        r -= 1
    
    r = row+1
    while r < size:
        if board[r][col] == 'K':
            return("Success")
        elif board[r][col] != '.':
            break
        r += 1
    
    c = col -1
    while c >= 0:
        if board[row][c] == 'K':
            return("Success")
        elif board[row][c] != '.':
            break
        c -= 1 
            
    c = col + 1
    while c < size:
        if board[row][c] == 'K':
            return "Success"
        elif board[row][c] != '.':
            break
        c +=1
        
    return "Fail"
#rook attack

def bishop_attack(board,row,col,size):

    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        if board[r][c] == 'K':
           return "Success"
            
        elif board[r][c] != '.':
            break

        r -= 1
        c -= 1

    r, c = row - 1, col + 1
    while r >= 0 and c < size:
        if board[r][c] == 'K':
            return "Success"
            
        elif board[r][c] != '.':
            break
           
        r -= 1
        c += 1

    r, c = row + 1, col - 1
    while r < size and c >= 0:
        if board[r][c] == 'K':
            return "Success"
            
        elif board[r][c] != '.':
            break
            
        r += 1
        c -= 1

    r, c = row + 1, col + 1
    while r < size and c < size:
        if board[r][c] == 'K':
            return "Success"
            
        elif board[r][c] != '.':
            break
           
        r += 1
        c += 1

    return  "Fail"
#bishop_attack
 
def queen_attack(board,row,col,size):
    if rook_attack(board,row,col,size) == "Success" or bishop_attack(board,row,col,size) == 'Success':
        return "Success"
    else:
        return "Fail"
#queen_attack
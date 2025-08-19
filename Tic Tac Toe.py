
#Step 1:
def display(r1):
    
    print('-------------------------------------------------------------------------------------')
    print(' '+r1[7]+'   |   '+r1[8]+'   |   '+r1[9])
    print('----------------------')
    print(' '+r1[4]+'   |   '+r1[5]+'   |    '+r1[6])
    print('----------------------')
    print(' '+r1[1]+'   |   '+r1[2]+'   |    '+r1[3])
    print('-------------------------------------------------------------------------------------')
    print('\n\n')


#Step 2:
def palyer_marker():
    marker = ''
    while marker not in ('X', 'O'):
        marker = input('Choose between X or O: ').upper()
        if marker not in ('X', 'O'):
            print('Invalid marker! Enter again.')

    if marker == 'X':
        return ('Null', 'X', 'O')   
    else:
        return ('Null', 'O', 'X')   

        

#Step 3:
def replacement_value(board,marker,position):
    board[position]=marker
    return board


#Step 4:
def check_win(board,marker):
    if board[1]==marker and board[2]==marker and board[3]==marker:
        return True
    elif board[7]==marker and board[8]==marker and board[9]==marker:
        return True
    elif board[4]==marker and board[5]==marker and board[6]==marker:
        return True
    elif board[1]==marker and board[5]==marker and board[9]==marker:
        return True
    elif board[7]==marker and board[5]==marker and board[3]==marker:
        return True
    elif board[7]==marker and board[4]==marker and board[1]==marker:
        return True
    elif board[8]==marker and board[5]==marker and board[2]==marker:
        return True
    elif board[9]==marker and board[6]==marker and board[3]==marker:
        return True
    else:
        return False


#Step 5:
import random
def chose_first():
    player=random.randint(1,2)
    if player==1:
        print('Player 1 go first!')
    elif player==2:
        print('Player 2 go first')
        
    return player  


#Step 6:
def space_check(board,position):
    return board[position]==' '



#Step 7:
def full_board_check(board):
    check=True
    for i in range(1,10):
        if board[i]==' ':
            check=False
            break
    
    return check


#Step 8:        
def position_choice():
    choice = '0'  # start as string so .isdigit() works
    
    while True:  # loop until we return a valid position
        choice = input('Pick a position from (1-9): ')
        
        if not choice.isdigit():
            print("Invalid input! Enter a number.")
            continue
        
        choice = int(choice)
        
        if choice not in range(1, 10):
            print("Invalid choice! Enter Again!")
            continue
        
        if not space_check(board, choice):
            print('Block filled, pick another position!')
            continue
        
        return choice  # only reached if everything is valid9



#Step 9:
def gameon_choice():
    choice='Wrong'
    
    while choice not in ['Y','N']:
        choice=input('Want a rematch ? (Y or N) ')
        
        if choice not in ['Y','N']:
            print('Invalid input!')
    
    if choice=='Y':
        return True
    else:
        return False    


def clear_output(board):
    board=[' ']*10
    return board


#STEP 10 (MAIN)
print('             Welcome to Tic Tac Toe!         ')

game_on=True
board=[' ']*11
markers=[]*3
first=chose_first()
markers=palyer_marker()
display(board) 

while game_on:
    print(f"Player {first} Turn: ")
    position = position_choice()
    board = replacement_value(board, markers[first], position)
    display(board)

    # check only current player's win
    if check_win(board, markers[first]):
        print(f"Player {first} Won!")
        game_on = gameon_choice()
        if game_on:
            board = clear_output(board)
            display(board)
        else:
            break

    elif full_board_check(board):
        print("Game Draw!")
        game_on = gameon_choice()
        if game_on:
            board = clear_output(board)
            display(board)
        else:
            break
    else:
        first = 2 if first == 1 else 1


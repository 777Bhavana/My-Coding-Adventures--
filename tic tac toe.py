

from random import randint
X='X'
O="O"



theBoard = {
            1 : '  ' , 2 : '  ',3 : '  ',
            4 : '  ' , 5 : '  ',6 : '  ',
            7 : '  ' , 8 : '  ',9 : '  ' 
          }

def printer (board):
    print( board[7] + '|' + board[8] +'|' + board[9])
    print('-----------')
    print( board[4] + '|' + board[5] +'|' + board[6])
    print('-----------')
    print( board[1] + '|' + board[2] +'|' + board[3])




def win(b,a):
    """
    the variable b is player and a is the computer
    """
    if theBoard[7]==theBoard[8]==theBoard[9] == b or theBoard[4]==theBoard[5]==theBoard[6] ==b or theBoard[1]==theBoard[2]==theBoard[3] ==b:
        print('the player '+ b +' won')
        exit()
                
    if theBoard[1]==theBoard[4]==theBoard[7] == b or theBoard[2]==theBoard[5]==theBoard[8] ==b or theBoard[3]==theBoard[6]==theBoard[9] ==b:
        print('the player ' + b +' won')
        exit()
        
                
    if theBoard[7]==theBoard[5]==theBoard[3] ==b or theBoard[1]==theBoard[5]==theBoard[9] ==b:
        print('the player ' + b +' won')
        exit()
                     
    if theBoard[7]==theBoard[5]==theBoard[3] ==a or theBoard[1]==theBoard[5]==theBoard[9] ==a or theBoard[1]==theBoard[4]==theBoard[7] == a or theBoard[2]==theBoard[5]==theBoard[8] ==a or theBoard[3]==theBoard[6]==theBoard[9] ==a or theBoard[7]==theBoard[8]==theBoard[9] == a or theBoard[4]==theBoard[5]==theBoard[6] ==a or theBoard[1]==theBoard[2]==theBoard[3] == a :
        print('the player '+a+" won")
        exit()
    
    

def play():
    count =0

    print('user/player  = \'X\' and computer  = \'O\'')
    while count<=9:
        w=True
        r =True
        while(w==True):
            
            player = int(input('Enter your move '))
            if theBoard[player] == "  ":
                count+=1
                theBoard[player] = 'X'
                printer(theBoard )
                print(' \n \n')
                w=False
            else :
                print('the block is taken please try again ')
                continue
        while(r==True): 
            computer = randint(1,9)
            if theBoard[computer] == "  ":
                count+=1
                theBoard[computer] ='O'
                printer(theBoard)
                print('\n\n')
                r=False
            else :
                continue
   
        if count>5:
            win(X,O)
            

                
            
            

play() 
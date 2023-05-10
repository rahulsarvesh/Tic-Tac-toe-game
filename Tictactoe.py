import winsound
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
player = 1  
Win = 1    
Draw = -1    
Running = 0    
Stop = 1    
Game = Running
      
def DrawBoard():    
    print("\n\t\t\t %c | %c | %c " % (board[1],board[2],board[3]))    
    print("\t\t\t___|___|___")    
    print("\t\t\t %c | %c | %c " % (board[4],board[5],board[6]))    
    print("\t\t\t___|___|___")    
    print("\t\t\t %c | %c | %c " % (board[7],board[8],board[9])) 
    print("\t\t\t   |   |   ")    
def CheckPosition(x):    
    if(board[x] == ' '):    
        return True    
    else:    
        return False    
       
def CheckWin():    
    global Game    
        
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
        Game = Win    
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
        Game = Win    
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
        Game = Win    
        
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        Game = Win    
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        Game = Win    
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
        Game=Win    

    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
        Game = Win    
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        Game=Win    
        
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
        Game=Draw    
    else:            
        Game=Running    
    
print("\t\t\tTic-Tac-Toe Game")    
print("\t\tPlayer 1 [X] --- Player 2 [O]\n")    
print()   
while(Game == Running):        
    DrawBoard()    
    if(player % 2 != 0):    
        print("Player 1's [X] chance")    
        Mark = 'X'    
    else:    
        print("Player 2's [O] chance")    
        Mark = 'O'    
    choice = int(input("Enter the position between [1-9] where you want to mark : "))  
    if(choice<=9 and choice>=1):
        if(CheckPosition(choice)):    
            board[choice] = Mark    
            player+=1    
            CheckWin()   
        else:
            print("\ninvalid choice") 
    else:
        print("\ninvalid choice")

        
        
DrawBoard()    
if(Game==Draw):    
    print("Game Draw")   
    winsound.Beep(2000,1000)
elif(Game==Win):    
    player-=1    
    if(player%2!=0):    
        print("Player 1 Won")
        winsound.Beep(2000,1000)    
    else:    
        print("Player 2 Won") 
        winsound.Beep(2000,1000)


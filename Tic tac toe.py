#!/usr/bin/env python
# coding: utf-8

# In[3]:


board=[" " for i in range(9)]#Create a board for the game
def draw_board():#This function draws a board every time its called.
    row1="|{}|{}|{}|".format(board[0],board[1],board[2])
    row2="|{}|{}|{}|".format(board[3],board[4],board[5])
    row3="|{}|{}|{}|".format(board[6],board[7],board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def victory(icon):#To print who won the game.we check for rows,columns, and diagonals.
    if (board[0]==board[1]==board[2]==icon or       board[3]==board[4]==board[5]==icon or       board[6]==board[7]==board[8]==icon or       board[0]==board[3]==board[6]==icon or       board[1]==board[4]==board[7]==icon or       board[2]==board[5]==board[8]==icon or       board[0]==board[4]==board[8]==icon or       board[6]==board[4]==board[2]==icon):
        return True
    else:
        return False
    
    
def move(icon):#This function is to ask the user for input move
    if icon=="X":
        playernum=1
    elif icon=="O":
        playernum=2
    print("your turn player {}".format(playernum))
    choice=int(input("enter choice between 1-9"))
    if board[choice-1]==" ":
        board[choice-1]=icon
    else:
        print("this place is full")
def draw_game():#If the game is draw it returns draw.
    if " " not in board:
        return True
    else:
        return False
        
while(True):#this loops runs as long as th game ends
    draw_board()
    move("X")
    draw_board()
    if victory("X"):
        print("player X wins")
        break
    elif draw_game():
        print("It's a draw game")
        break  
    move("O")
    if victory("O"):
        draw_board()
        print("player O wins")


# 

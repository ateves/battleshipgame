from random import randint 
#board statement/variable
board = []

#this for loop sets the range in place
for x in range(0, 5):
  board.append(["O"] * 5)

#this method is what places the board in a way that removes/dismembers all the commas, quotations, and brackets.
def print_board(board):
  for row in board:
    print(" ".join(row))

#prints out a board template for us
print_board(board)

#this method sets the board in place
def random_row(board_in):
  #this line of code sets a variable called row and calls it as a range of numbers between 0 and the length of the board in a row
  row = randint(0, len(board_in)-1)
  return row

#see above but in columns instead of rows
def random_col(board_in):
  column = randint(0, len(board_in)-1)
  return column

#this is the ships row and column
ship_row = random_row(board)
ship_col = random_col(board)

#print statement for above
print(ship_row + 1)
print(ship_col + 1)

#print statements for column and boards (triggers)
#print(random_col(board))
#print(random_row(board))

#This is where the program is asking us to input our own rows and columns
guess_row = int(input("Guess Row: "))-1
guess_col = int(input("Guess Col: "))-1

not_hit=True
while not_hit:
  # This is a for loop accessing a guess
  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sank my battleship!")
    not_hit=False
  else: 
    print("you missed my battleship!")
    board[guess_row][guess_col] = "X"
    print_board(board)
    guess_row = int(input("Guess Row: "))-1
    guess_col = int(input("Guess Col: "))-1
    
  

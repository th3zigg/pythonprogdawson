# Tic-Tac-Toe
# Plays the game of tic-tac-tow against a human opponent

# global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def display_instruct():
  """Display game instructions."""
  print(
  """
  Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
  This will be a showdown between your human brain and my silicon processor.

  You will make your move known by entering a number, 0 - 8.  The number
  will correspond to the board position as illustrated:

            0 | 1 | 2
            ---------
            3 | 4 | 5
            ---------
            6 | 7 | 8

  Prepare yourself, human.  The ultimate battle is about to begin. \n
  """
  )

def ask_yes_no():
  """Ask a yes or no question."""
  response = None
  while response not in ("y","n"):
    response = input(question).lower()
  return response

def ask_number(question, low, high):
  """Ask for a number within a range."""
  response = None
  while response not in range(low, high):
    response = int(input(question))
  return response

def pieces():
  """Determine if player or computer goes first."""
  go_first = ask_yes_no("Do you require the first move? (y/n): ")
  if go_first == "y":
    print("\nThen take first move. You will need it.")
    human = X
    computer = O
  else:
    print("\nYour bravery will be your undoing... I wil go first.")
    computer = X
    human = O
  return computer, human

def new_board():
  """Create new game board."""
  board[]
  for square in range(NUM_SQUARES):
    board.append(EMPTY)
  return board

def display _board(board):
  """Display game board on screen."""
  print("\n\t", board[0], "|", board[1], "|", board[2])
  print("t", "---------")
  print("\n\t", board[3], "|", board[4], "|", board[5])
  print("t", "---------")
  print("\n\t", board[6], "|", board[7], "|", board[8])

def lega_moves(board):
  """Create a list of legal moves"""
  moves = []
  for square in range(NUM_SQUARES):
    if board[square] == EMPTY:
      moves.append(square)
  return moves

def winner(board):
  """Determine the game winner."""
  WAYS_TO_WIN = ((0, 1, 2),
                 (3, 4, 5),
                 (6, 7, 8),
                 (0, 3, 6),
                 (1, 4, 7),
                 (2, 5, 8),
                 (0, 4, 8),
                 (2, 4, 6))
  for row in WAYS_TO_WIN:
    if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
      winner = board[row[0]]
      return winner
  if EMPTY not in board:
      return TIE
  return NONE

def human_move(board, human):
  """Get human move."""
  legal = legal_moves(board)
  move = None
  while move not in legal:
    move = ask_number("Where will you move? (0 - 8):", 0, NUM_SQUARES)
    if move not in legal:
      print("\nThat square is already occupied, foolish human. Choose another.\n")
  print("Fine...")
  return move

def computer_move(board, computer, human):  
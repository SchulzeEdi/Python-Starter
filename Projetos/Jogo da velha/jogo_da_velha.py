import random 
import os

class ticTacToe:
  def __init__(self) -> None:
    self.board = [[" "," "," "], [" "," "," "], [" "," "," "]]
    self.done = ""
  def print_board(self):
    print("")
    print(" " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2])
    print("-----------")
    print(" " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2])
    print("-----------")
    print(" " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2])

  def reset_board(self):
    self.board = [[" "," "," "], [" "," "," "], [" "," "," "]]
    self.done = ""

  def check_win_or_draw(self):
    dict_win = {"X": False, "O": False}
    for i in ["X", "O"]:
      #Horizontal
      dict_win[i] = (self.board[0][0] == self.board[0][1] == self.board[0][2] == i)
      dict_win[i] = (self.board[1][0] == self.board[1][1] == self.board[1][2] == i) or dict_win[i]
      dict_win[i] = (self.board[2][0] == self.board[2][1] == self.board[2][2] == i) or dict_win[i]
      #Vertical
      dict_win[i] = (self.board[0][0] == self.board[1][0] == self.board[2][0] == i) or dict_win[i]
      dict_win[i] = (self.board[0][1] == self.board[1][1] == self.board[2][1] == i) or dict_win[i]
      dict_win[i] = (self.board[0][2] == self.board[1][2] == self.board[2][2] == i) or dict_win[i]

      #Diagonal
      dict_win[i] = (self.board[0][0] == self.board[1][1] == self.board[2][2] == i) or dict_win[i]
      dict_win[i] = (self.board[2][0] == self.board[1][1] == self.board[0][2] == i) or dict_win[i]

      if dict_win["X"]:
        self.done = "x"
        print("X venceu!")
        return
      elif dict_win["O"]:
        self.done = "o"
        print("O venceu!")
        return

      c = 0
      for i in range(3):
        for j in range(3):
          if self.board[i][j] != " ":
            c+=1
            break
      if c == 0:
        self.done = "d"
        print("Empate!")
        return
      
  def get_player_move(self):
    invalid_move=True

    while invalid_move:      
      try:
        print("Digite a linha do seu proximo lance:")
        x = int(input())

        print("Digite a coluna do seu proximo lance:")
        y = int(input())

        if x > 2 or x < 0 or y > 2 or y < 0:
          print("Coordenadas invalidas")

        if self.board[x][y] != " ":
          print("Posicao ja preenchida")
          continue
      except Exception as e:
        print(e)
        continue
      invalid_move = False
    self.board[x][y] = "X"

  def make_move(self):
    list_move = []

    for i in range(3):
      for j in range(3):
        if self.board[i][j] == " ":
          list_move.append((i,j))
    if len(list_move) > 0:
      x, y = random.choice(list_move)
      self.board[x][y] = "O"

ticTacToe = ticTacToe()
ticTacToe.print_board()
next = 0

while next == 0:
  os.system("clear")
  ticTacToe.print_board()
  while ticTacToe.done == "":
    ticTacToe.get_player_move()
    ticTacToe.make_move()

    os.system("clear")

    ticTacToe.print_board()
    ticTacToe.check_win_or_draw()
  print("Digite 1 para sair ou qualquer tecla para continuar jogando")
  next = int(input())
  if next == 1:
    break
  else:
    ticTacToe.reset_board()
    next = 0
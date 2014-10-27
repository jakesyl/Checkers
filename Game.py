from random import randint

#Classes for Game Pieces
class checker(object):
  def __init__(self,team,x,y):
    self.team = team
    self.x = x
    self.y = y
  def move(move):
    y = y+1
    if move == "left":
      x = x+1
      if x > 1:
        x = x-1
        print ("Incorrect Move. Loss of Turn")
    elif move == "right":
      x = x-1
      if x < 1:
        x = x + 1
        print ("Incorrect Move. Loss of Turn")
    else:
      print ("Incorrect Move. Loss of Turn")
class king(checker):
  def move(up,side):
    if up == "up":
      y = y+1
      if y > 8:
          y = y-1
          print ("Incorrect Move. Loss of Turn")
    elif up == "down":
      y = y-1
      if y < 1:
          y = y+1
          print ("Incorrect Move. Loss of Turn")
    else:
      print ("Incorrect Move. Loss of Turn")
    if move == "left":
      x = x+1
      if x > 8:
          x = x-1
          print ("Incorrect Move. Loss of Turn")
    elif move == "right":
      x = x-1
      if x < 1:
          x = x+1
          print ("Incorrect Move. Loss of Turn")
    else:
      print ("Incorrect Move. Loss of Turn")
def check_king(checker):
   if checker.y > 8:
     checker = king(checker.team, checker.x, checker.y)
     checker.y = checker.y - 1

#Adding Checkers
red1 = checker("red", 2, 1)
red2 = checker("red", 4, 1)
red3 = checker("red", 6, 1)
red4 = checker("red", 8, 1)
red5 = checker("red", 1, 2)
red6 = checker("red", 3, 2)
red7 = checker("red", 5, 2)
red8 = checker("red", 7, 2)
red9 = checker("red", 2, 3)
red10 = checker("red", 4, 3)
red11 = checker("red", 6, 3)
red12 = checker("red", 8, 3)

black1 = checker("black", 1, 8)
black2 = checker("black", 3, 8)
black3 = checker("black", 5, 8)
black4 = checker("black", 7, 8)
black5 = checker("black", 2, 7)
black6 = checker("black", 4, 7)
black7 = checker("black", 6, 7)
black8 = checker("black", 8, 7)
black9 = checker("black", 1, 6)
black10 = checker("black", 3, 6)
black11 = checker("black", 5, 6)
black12 = checker("black", 7, 6)

#Giving Checkers to Each Player
user_checkers = [red1, red2, red3, red4, red5, red6, red7, red8, red9, red10, red11, red12]
cpu_checkers = [black1, black2, black3, black4, black5, black6, black7, black8, black9, black10, black11, black12]

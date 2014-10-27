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
        if x > 8:
          x = x-1
          print ("Incorrect Move. Loss of Turn")
    elif move == "right":
      x = x-1
        if x < 0:
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
      if y < 0:
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
      if x < 0:
          x = x+1
          print ("Incorrect Move. Loss of Turn")
    else:
      print ("Incorrect Move. Loss of Turn")
  def check_king(checker):
    if checker.y > 8:
      checker = king(checker.team, checker.x, checker.y)
      checker.y = checker.y - 1

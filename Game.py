from random import randint

#Add Classes for Game Pieces
class checker(object):
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def move(move):
    y = y+1
    if move == "left":
      x = x+1
    elif move == "right":
      x = x-1
    else:
      print ("Incorrect Move. Loss of Turn")
class king(checker):
  def move(up,side):
    if up == "up":
      y = y+1
    elif up == "down":
      y = y-1
    else:
      print ("Incorrect Move. Loss of Turn")
    if move == "left":
      x = x+1
    elif move == "right":
      x = x-1
    else:
      print ("Incorrect Move. Loss of Turn")

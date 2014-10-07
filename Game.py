from random import randint

#Add Classes for Game Pieces
class checker:
  def __init__(self,pos):
    self.pos = [pos[0],pos[1]]# its a list x and y pos based on id
    self.gamewin = game()
    self.uid = pos[0]
  def move():
    game.checkwin(self.gamewin, self.pos,self.uid)
    
class game:
  def check_win(self, pos, uid):
    pass
    

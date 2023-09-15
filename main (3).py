#define the base class player
class player:
  def play(self):
    print("The player is playing cricket.") 
# define the derived class batsman
class batsman(player):
  def play(self):
    print("The batsman is bating")
#define the derived class bowler
class bowler(player):
  def play(self):
    print("The bowler is bowling")
#create objects of batsman and bowler clases
batsman=batsman()
bowler=bowler()
#call the play method for each object 
batsman.play()
bowler.play()
          

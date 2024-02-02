import time
class VideoGame:
  def __init__(self, name, size):
    self.name = name
    self.size = size
  def play_game(self):
    print("Playing {}...".format(self.name))
  
class Computer:
  disk_space = 500
  def __init__(self, name):
    self.name = name
    self.downloaded_games = []
  def download(self, game):
    if self.disk_space >= game.size:
      self.downloaded_games.append(game)
      self.disk_space -= game.size
      print("{} has been downloaded".format(game.name))
    else:
      print("{} could not be downloaded".format(game.name))
  def play_game(self, game):
    game.play_game()
  def delete_game(self, game):
    self.downloaded_games.remove(game)
  def get_total_size(self):
    total_size = 0
    for game in self.downloaded_games:
      total_size += game.size
    return total_size
  def get_free_space(self):
    return self.disk_space
  def get_used_space(self):
    return self.get_total_size() - self.get_free_space()

my_computer = Computer("MacBook Pro")
my_game = VideoGame("Call of Duty", 30)
my_computer.download(my_game)
print(my_computer.get_free_space())
print(my_computer.get_used_space())
my_computer.play_game(my_game)
my_computer.delete_game(my_game)
print(my_computer.get_total_size())
time.sleep(1)
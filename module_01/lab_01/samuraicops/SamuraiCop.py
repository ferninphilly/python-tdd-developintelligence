class SamuraiCop:

  def __init__(self, name, badguys):
    self.name = name
    self.badguys = badguys
    self.cop = True
    self.chickens = 0

  def bad_guys_beaten_up(self):
    beatenup = self.badguys.pop()
    print(self.name + "  just beat up " + beatenup + "\n")
    print(str(len(self.badguys)) + " remain!")
    print("Next bad guy is: " + self.badguys[-1])
    return beatenup
  
  def you_are_fired(self):
    if self.cop:
      self.cop = False
    else:
      self.cop = True
    print("Is " + self.name + " a cop any more?")
    print(self.cop)

  def birthday_chickens_killed(self):
    print("It's " + self.name + "'s birthday?")
    print("How many neighbor's chickens killed?")
    self.chickens += 1
    print(str(self.chickens) + " chicken killed for birthday meals!")
  
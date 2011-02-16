class Message:
  
  def __init__(self, message, number, time):
    self.time = time
    self.message = message
    self.number = number
  
  def __lt__(self, that):
    return self.time <= that.time

  def get_data(self):
    return (self.number, self.message, self.time)


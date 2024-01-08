class Response:
  def __init__(self, name, num_engagements):
      self.name = name
      self.num_engagements = num_engagements

  def display_info(self):
      print(f"Behavior: {self.name}")
      print(f"Number of Engagements: {self.num_engagements}")
# maybe make this a dictionary instead?


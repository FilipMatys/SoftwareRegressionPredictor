from models.Token import Token

class NumericalToken(Token):
   def __init__(self, name):
      self.name = name
      self.value = 0
# Represents structure, that holds change data for 
class StructureDiff:
   # Initialize structure diff
   def __init__(self, type):
      self.type = type
      self.tokens = []

   # Add token
   def addToken(self, token):
      self.changeTokens.append(token)
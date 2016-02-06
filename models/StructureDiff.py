# Represents structure, that holds change data for 
class StructureDiff:
   # Initialize structure diff
   def __init__(self, type):
      self.type = type
      self.changeTokens = []
      self.numericalTokens = []

   # Add change token
   def addChangeToken(self, token):
      self.changeTokens.append(token)

   # Add numerical token
   def addNumericalToken(self, token):
      self.numericalTokens.append(token)
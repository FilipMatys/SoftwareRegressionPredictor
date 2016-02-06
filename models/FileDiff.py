# Difference for a file
class FileDiff:
   # Initialize file diff
   def __init__(self, name):
       self.name = name
       self.structures = []

   # Add structure
   def addStructure(self, structure):
       self.structures.append(structure)
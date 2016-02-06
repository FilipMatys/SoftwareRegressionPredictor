# Wrapper for all commit changes
class CommitDiff:
   # Initialize difference
   def __init__(self):
      self.files = []

   # Add file to difference list
   def addFile(self, file):
      self.files.append(file)
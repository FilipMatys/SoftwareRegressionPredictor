# Difference for a file
class FileDiff:
    # Initialize file diff
    def __init__(self, name):
        self.name = name
        self.tokens = dict()

    def getVars(self):
        return vars(self)
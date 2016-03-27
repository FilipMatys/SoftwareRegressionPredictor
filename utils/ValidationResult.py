class ValidationResult(object):
    def __init__(self, data):
        self.data = data
        self.errors = []
        self.isValid = True

    def addError(self, message):
        self.errors.append(message)
        self.isValid = False

    def append(self, validation):
        self.errors = self.errors + validation.errors
        self.isValid = self.isValid and validation.isValid

        return self.isValid

    def getVars(self):
        return vars(self)



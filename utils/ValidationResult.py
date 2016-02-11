class ValidationResult(object):
    def __init__(self, data):
        self.data = data
        self.errors = []
        self.isValid = True

    def addError(self, message):
        self.errors.append(message)
        self.isValid = False



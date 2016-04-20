class ValidationResult(object):
    def __init__(self, data):
        self.data = data
        self.errors = []
        self.warnings = []
        self.isValid = True

    def addError(self, message):
        self.errors.append(message)
        self.isValid = False

    def addWarning(self, message):
        self.warnings.append(message)

    def append(self, validation):
        self.warnings = self.warnings + validation.warnings
        self.errors = self.errors + validation.errors
        self.isValid = self.isValid and validation.isValid

        return self.isValid

    def getVars(self):
        return vars(self)



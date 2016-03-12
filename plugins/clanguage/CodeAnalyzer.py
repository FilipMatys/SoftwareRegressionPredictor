import re, random, string

class CodeAnalyzer(object):
    # Constants
    CYCLE = "Cycle"
    FLOW_CHANGE = "Flow change"
    ASSIGNMENT = "Assignment"
    CONDITION = "Condition"
    RETURN_STATEMENT = "Return statement"
    STRUCTURE_OR_ENUMERATION = "Structure or enumeration"
    INCLUSION = "Inclusion"
    MEMORY_FUNCTION = "Memory function"
    STRING_MANIPULATION = "String manipulation"
    MULTIBYTE_FUNCTION = "Multibyte function"
    STRING_FUNCTION = "String function"
    PROCESSING_DIRECTIVE = "Processing directive"
    ARRAY = "Array"
    CONSTANT = "Constant"
    STORAGE_CLASS_SPECIFIER = "Storage class specifier"
    LINE = "Line"

    # Initialize object with file diff
    def __init__(self, fileDiff):
        self.fileDiff = fileDiff

    """ Analyze file """
    def analyze(self):
        # Init object for added and removed characteristics
        added = self.initializeDifferenceObject()
        addedLines = []
        removed = self.initializeDifferenceObject()
        removedLines = []

        # Iterate through changed lines
        for (old, new, row) in self.fileDiff[1]:
            # Removed line
            if new is None:
                removed[self.LINE] += 1
                removed = self.analyzeRow(row, removed)
                removedLines.append(row)
            # Added line
            if old is None:
                added[self.LINE] += 1
                added = self.analyzeRow(row, added)
                addedLines.append(row)
        
        # Return added and removed characteristics
        return {
            "name": self.fileDiff[0][3], 
            "added": { "changes": added, "lines": addedLines },
            "removed": { "changes": removed, "lines": removedLines }
        }      
       
    """ Analyze row """
    def analyzeRow(self, row, difference):
        # Cycle
        if self.hasCycle(row): difference[self.CYCLE] += 1
        # Flow change
        if self.hasFlowChange(row): difference[self.FLOW_CHANGE] += 1
        # Assignment
        if self.hasAssignment(row): difference[self.ASSIGNMENT] += 1
        # Condiftion
        if self.hasCondition(row): difference[self.CONDITION] += 1
        # Return statement
        if self.hasReturnStatement(row): difference[self.RETURN_STATEMENT] += 1
        # Structure and enumeration
        if self.hasStructOrEnum(row): difference[self.STRUCTURE_OR_ENUMERATION] += 1
        # Inclusion
        if self.hasInclude(row): difference[self.INCLUSION] += 1
        # Memory function
        if self.hasMemoryFunction(row): difference[self.MEMORY_FUNCTION] += 1
        # String modification
        if self.hasStringManipulationFunction(row): difference[self.STRING_MANIPULATION] += 1
        # Multibyte function
        if self.hasMultibyteFunction(row): difference[self.MULTIBYTE_FUNCTION] += 1
        # String function
        if self.hasStringFunction(row): difference[self.STRING_FUNCTION] += 1
        # Processing directive
        if self.hasPreprocessingDirectives(row): difference[self.PROCESSING_DIRECTIVE] += 1
        # Array
        if self.hasArray(row): difference[self.ARRAY] += 1
        # Constant
        if self.hasConstant(row): difference[self.CONSTANT] += 1
        # Storage class specifier
        if self.hasStorageClassSpecifier(row): difference[self.STORAGE_CLASS_SPECIFIER] += 1

        return difference

    """ Initialize object for difference """
    def initializeDifferenceObject(self):
        return {
            self.CYCLE: 0,
            self.FLOW_CHANGE: 0,
            self.ASSIGNMENT: 0,
            self.CONDITION: 0,
            self.RETURN_STATEMENT: 0,
            self.STRUCTURE_OR_ENUMERATION: 0,
            self.INCLUSION: 0,
            self.MEMORY_FUNCTION: 0,
            self.STRING_MANIPULATION: 0,
            self.MULTIBYTE_FUNCTION: 0,
            self.STRING_FUNCTION: 0,
            self.PROCESSING_DIRECTIVE: 0,
            self.ARRAY: 0,
            self.CONSTANT: 0,
            self.STORAGE_CLASS_SPECIFIER: 0,
            self.LINE: 0
        }

    """ Check for cycle """
    def hasCycle(self, row):
        return re.search(r"(for|while|do)", row)

    """ Check for flow change """
    def hasFlowChange(self, row):
        return re.search(r"(goto|break|continue|switch|case)", row)
    
    """ Check for assignment """
    def hasAssignment(self, row):
        return re.search(r"=", row)

    """ Check for condition """
    def hasCondition(self, row):
        if "?" in row and ":" in row:
            return True

        return re.search(r"(if|else)", row)

    """ Check for return statement """
    def hasReturnStatement(self, row):
        return re.search(r"return", row)

    """ Check for struct or enum """
    def hasStructOrEnum(self, row):
        return re.search(r"(struct|union)", row)

    """ Check for include """
    def hasInclude(self, row):
        return re.search(r"#include", row)

    """ Check for memory function """
    def hasMemoryFunction(self, row):
        return re.search(r"(calloc|malloc|free|realloc)", row)

    """ Check for string function """
    def hasStringFunction(self, row):
        return re.search(r"(atof|atoi|atol|strtod|strtol|strtoul)", row)

    """ Check for multi byte function """
    def hasMultibyteFunction(self, row):
        return re.search(r"(mblen|mbstowcs|mbtowc|wcstombs|wctomb)", row)

    """ Check for string manipulation function """
    def hasStringManipulationFunction(self, row):
        return re.search(r"(memchr|memcmp|memcpy|memmove|memset|strcat|strncat|strchr|strcmp|strncmp|strcoll|strcpy|strncpy|strcspn|strerror|strlen|strpbrk|strrchr|strspn|strstr|strtok|strxfrm)", row)

    """ Check if has preprocessing directives """
    def hasPreprocessingDirectives(self, row):
        return re.search(r"(#if|#elif|#else|#endif|#define|#undef|#ifdef|#ifndef|#include|#line|#error|#pragma)", row)

    """ Check if uses array """
    def hasArray(self, row):
        if "[" in row and "]" in row:
            return True

        return None

    """ Check if has constant """
    def hasConstant(self, row):
        return re.search(r"const", row)

    """ Check for storage class specifier """
    def hasStorageClassSpecifier(self, row):
        return re.search(r"(typedef|extern|static|auto|register)", row)


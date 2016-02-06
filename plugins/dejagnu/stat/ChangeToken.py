from enum import Enum
from models.Token import Token

# Token reprezenting character of change
class ChangeToken(Token, Enum):
   # Added new function or structure
   STRUCT_ADDED = 1
   # Removed function or structure
   STRUCT_REMOVED = 2
   # Added memory function
   MEMORY_FUNCTION_ADDED = 3
   # Removed memory function
   MEMORY_FUNCTION_REMOVED = 4
   # Modified memory function
   MEMORY_FUNCTION_MODIFIED = 5
   # Added new condition
   CONDITION_ADDED = 6
   # Removed condition
   CONDITION_REMOVED = 7
   # Modified condition   
   CONDITION_MODIFIED = 8
   # Added cycle
   CYCLE_ADDED = 9
   # Removed cycle
   CYCLE_REMOVED = 10
   # Modified cycle
   CYCLE_MODIFIED = 11
   # Modified code flow
   FLOW_MODIFIED = 12
   # Deletion
   DELETION = 13
   # Addition
   ADDITION = 14
   # Modification
   MODIFICATION = 15
   # Added literal
   LITERAL_ADDED = 16
   # Removed literal
   LITERAL_REMOVED = 17
   # Function call
   FUNCTION_CALL = 18
   # Variable initialization
   VARIABLE_INIT = 19
   # Calculation
   CALCULATION = 20
   # Added commentary
   COMMENT_ADDED = 21
   # Removed commentary
   COMMENT_REMOVED = 22
   # Modified commentary
   COMMENT_MODIFIED = 23
   # Data type change
   DATA_TYPE_CHANGE = 24
   # User funcion called
   USER_FUNC_CALL = 25
   # System func call
   SYS_FUNC_CALL = 26
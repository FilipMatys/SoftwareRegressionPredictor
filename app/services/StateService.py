from utils.ValidationResult import ValidationResult
from app import app
import config

class StateService(object):
    """description of class"""

    """ Set application state """
    def set(state):
        app.config[config.POLLING_KEY] = state

    """ Reset application state """
    def reset():
        app.config[config.POLLING_KEY] = "Nothing is happening"

    """ Get current state """
    def poll():
        # Init validation
        validation = ValidationResult({"State": ""})

        # Check if session is set
        if config.POLLING_KEY not in app.config:
            StateService.reset()        

        validation.data["State"] = app.config[config.POLLING_KEY]
        

        # Return validation
        return validation



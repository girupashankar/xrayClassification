import os
import sys

def error_message_detail(error: Exception, error_details: sys) -> str:
    # Retrieve traceback details
    _, _, exc_tb = sys.exc_info()
    # Extract file name where the error occurred
    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    # Format the error message
    error_message = "Error occurred in Python script: [{0}], line number: [{1}], error message: [{2}].".format(
        file_name, exc_tb.tb_lineno, str(error))
    
    return error_message
class XrayException(Exception):
    def __init__(self, error_message, error_details):
        """
        Initialize the custom exception with a message and additional details.
        
        :param error_message: The main message for the exception in string format.
        :param error_details: A dictionary containing additional details about the exception.
        """
        super().__init__(error_message)
        # Check that error_details is a dictionary
        if not isinstance(error_details, dict):
            raise ValueError("Error details must be provided as a dictionary.")
        # Format and store the detailed error message
        self.error_message = self.format_error_message(error_message, error_details)
    
    def __str__(self):
        return self.error_message
    
    @staticmethod
    def format_error_message(message, details):
        """
        Format the detailed error message using both the provided message and additional details.
        
        :param message: The main error message.
        :param details: A dictionary of error details.
        :return: A formatted string representing the complete error information.
        """
        detail_parts = [f"{key}: {value}" for key, value in details.items()]
        detailed_message = f"{message} | Details: " + ", ".join(detail_parts)
        return detailed_message

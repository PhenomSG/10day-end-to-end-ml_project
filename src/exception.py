"""
url: https://docs.python.org/3/library/exceptions.html
"""

# Project Exception Handling

import sys

def error_message_detail(error, err_detail: sys):
    _, _, exc_tb = err_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    return "Error occurred in script [{0}] at line [{1}] with error: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

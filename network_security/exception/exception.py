import sys
from network_security.logging import logger

def error_message_details(error: Exception, error_details:sys) -> str:
    _,_,exc_tb = error_details.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno

    error_message = (
        f"error file name is - {file_name}\n"
        f"error line no is - {line_no}\n"
        f"error message = {str(error)}"
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error_message:Exception, error_details:sys):
        super().__init__(error_message)

        self.error_message = error_message_details(error_message, error_details)

    def __str__(self):
        return self.error_message
    



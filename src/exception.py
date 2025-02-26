import sys
import os


def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()

    file_name=exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno

    error_message = f"error occured and the file name is {file_name} and the linenumber is {line_no} and error is {error}"

    return error_message


class SensorException(Exception):

    def __init__(self,error_message,error_detail:sys):
        # aa first constructor no error message aapde 2nd constructor ma aapyo bcz It ensures SensorException behaves like a normal Python exception
      

        super().__init__(error_message)
        

        self.error_message = error_message_detail(error_message,error_detail=error_detail)
        

    def __str__(self):
        return self.error_message


import os
import sys  #inherite exception class present first using os sys then custom exception for ur projrct

class HousingException(Exception):
    # error_message is object for exception class
    def __init__(self, error_message:Exception,error_detail:sys):#sys module used to execution details and  declare which line,file causing error
        super().__init__(error_message) #super is parent class initlaiser i.e exception u can write exception(error_message)
        self.error_message=HousingException.get_detailed_error_message(error_message=error_message,
                                                                       error_detail=error_detail
                                                                        )


    @staticmethod
    def get_detailed_error_message(error_message:Exception,error_detail:sys)->str: #-> is nothing but return of fun here it returns string 
        """
        error_message: Exception object
        error_detail: object of sys module
        """
        _,_ ,exec_tb = error_detail.exc_info()  # _,_ blank spaces for type and value which we dont want from exc_info() #exc_info gives recent exception
        exception_block_line_number = exec_tb.tb_frame.f_lineno
        try_block_line_number = exec_tb.tb_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message = f"""
        Error occured in script: 
        [ {file_name} ] at 
        try block line number: [{try_block_line_number}] and exception block line number: [{exception_block_line_number}] 
        error message: [{error_message}]
        """
        return error_message

    def __str__(self): # how object for class should be represent in print 
        return self.error_message


    def __repr__(self) -> str:#how object for class should be represent without print
        return HousingException.__name__.str()
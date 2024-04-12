# Python: Get the Type, File and Line Number of Exception

import sys
import os

try:
    raise ValueError('invalid value')
except ValueError as e:
    e_type, e_object, e_traceback = sys.exc_info()

    e_filename = os.path.split(
        e_traceback.tb_frame.f_code.co_filename
    )[1]

    e_message = str(e)

    e_line_number = e_traceback.tb_lineno

    print(f'exception type: {e_type}')

    print(f'exception filename: {e_filename}')

    print(f'exception line number: {e_line_number}')

    print(f'exception message: {e_message}')
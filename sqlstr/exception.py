'''
Exceptions from sqlstr
-------------------------
'''


class sqlstrException(Exception):
    def __init__(self, message):
        '''
        Instanitates a custom sqlstrException

        message -- string. Message describing the exception.
        '''
        Exception.__init__(self, message)

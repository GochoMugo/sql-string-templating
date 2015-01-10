'''
Exceptions from sqlstr
-------------------------
'''


class sqlstrException(Exception):
    def __init__(self, message):
        '''
        Instanitates a custom sqlstrException
        :message str:
        '''
        Exception.__init__(self, message)

'''
Runs tests against exceptions defined in ``exception.py``
'''

import unittest
from sqlstr import exception


class Test_Exceptions(unittest.TestCase):
    '''Test suite for sqlstr.exception'''

    def test_sqlstrException(self):
        '''Test the base exception sqlstr.exception.sqlstrException'''
        test_exception = exception.sqlstrException("some exception")
        self.assertIsInstance(test_exception, Exception,
            "exception.sqlstrException is not a sub-class of Exception")

'''
Runs tests against the language MySQL language
'''


import unittest
import sqlstr


class Test_MySQL(unittest.TestCase):
    '''Test suite for sqlstr.MySQL'''

    def test_basic(self):
        '''Test basic properties of sqlstr.MySQL class'''
        self.assertTrue(issubclass(sqlstr.MySQL, sqlstr.Base),
            "sqlstr.MySQL does not sub-class sqlstr.Base")

'''
Runs tests against the SQLite3 Language
'''


import unittest
import sqlstr


class Test_SQLite3(unittest.TestCase):
    '''Test suite for sqlstr.SQLite3'''

    def test_basic(self):
        '''Test basic properties of sqlstr.SQLite3'''
        self.assertTrue(issubclass(sqlstr.SQLite3, sqlstr.Base),
            "sqlstr.SQLite3 does not sub-class sqlstr.Base")

    def test_redefines_lang_pack(self):
        '''Test that sqlstr.SQLite3 redefines its language pack'''
        base_pack = sqlstr.Base.lang_pack
        sqlite3_pack = sqlstr.SQLite3.lang_pack
        self.assertNotEqual(base_pack, sqlite3_pack,
            "sqlstr.SQLite3 fails to redefine its language pack")

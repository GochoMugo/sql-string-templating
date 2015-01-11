'''
Runs test against the Base language class
'''


import unittest
from sqlstr.Base import *


class Test_Base(unittest.TestCase):
    '''Test suite for sqlstr.common.Base class'''

    def test_Base_class_variables(self):
        '''Test for pre-defined class variables in sqlstr.Base'''
        self.assertIsNotNone(Base.lang_pack, "sqlstr.Base class has no variable, lang_pack")
        self.assertIsNotNone(Base.context, "sqlstr.Base class has no variable, context")

    def test_Base_get_string(self):
        '''Test class method sqlstr.Base.get_string'''
        test_lang = { "show_tables": "SHOW ALL TABLES;" }
        @update_pack(test_lang)
        @language
        class JokeLang(Base):
            pass
        result = JokeLang.get_string("show_tables")
        self.assertIsInstance(result, str,
            "sqlstr.Base,get_string does not return a string")
        self.assertEqual(result, test_lang["show_tables"],
            "sqlstr.Base.get_string does not return same template string. %s != %s"
            % ("show_tables", result))

    def test_Base_allows_lang_update(self):
        '''Test class method sqlstr.Base.update'''
        test_lang = { "show_tables": "SHOW ALL TABLES;" }
        @update_pack(test_lang)
        @language
        class JokeLang(Base):
            pass
        self.assertEqual(JokeLang.get_string("show_tables"), test_lang["show_tables"],
            "Sub-classes can not update the language pack")

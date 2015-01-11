import unittest
from sqlstr import Base


class Test_Base(unittest.TestCase):
    def test_class_variables(self):
        self.assertIsNotNone(Base.lang_pack, "sqlstr.Base class has no variable, lang_pack")
        self.assertIsNotNone(Base.context, "sqlstr.Base class has no variable, context")

    def test_update(self):
        
        class JokeLang(Base):
            pass
        JokeLang.update()

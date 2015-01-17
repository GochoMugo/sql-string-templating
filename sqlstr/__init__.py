'''
=====
sqlstr
=====

Experimental use of a Language table to solve SQL variants.

See Discussion related to this: https://github.com/firstprayer/monsql/pull/10
Some research/must-read: https://www.udemy.com/blog/sql-queries/
'''

__version__ = "0.0.0-alpha.1.0"


from .Base import Base, language, lang_pack
from .MySQL import MySQL
from .SQLite3 import SQLite3


__all__ = ["__version__", "Base", "language", "lang_pack", "MySQL", "SQLite3",]

'''
=====
sqlstr
=====

Experimental use of a Language table to solve SQL variants.

See Discussion related to this: https://github.com/firstprayer/monsql/pull/10
Some research/must-read: https://www.udemy.com/blog/sql-queries/
'''

__version__ = "0.0.0"


from .common import Base
from .MySQL import MySQL
from .SQLite3 import SQLite3


__all__ = ["__version__", "Base", "MySQL", "SQLite3",]

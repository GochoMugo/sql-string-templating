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


__all__ = ["Base", "__version__"]

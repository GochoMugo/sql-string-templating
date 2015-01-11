'''
SQLite3-specific strings
--------------------------

Strings generated from this module are specific to SQLite3.
'''


from common import Base


SQLite3_pack = {
  "show_tables": "SELECT name FROM sqlite_master WHERE type = 'table';"
}


class SQLite3(Base):
  pass

SQLite3.update(SQLite3_pack)

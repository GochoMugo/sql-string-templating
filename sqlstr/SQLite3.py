'''
SQLite3-specific strings
--------------------------

Strings generated from this module are specific to SQLite3.
'''


from .Base import Base, language, update_pack


SQLite3_pack = {
  "show_tables": "SELECT name FROM sqlite_master WHERE type = 'table';"
}


@update_pack(SQLite3_pack)
@language
class SQLite3(Base):
    pass

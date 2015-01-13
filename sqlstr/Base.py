'''
Experimental use of a Language table to solve SQL variants.

See Discussion related to this: https://github.com/firstprayer/monsql/pull/10
Some research/must-read: https://www.udemy.com/blog/sql-queries/

Values preceded with ``$``, for example, $table_name, are placeholders in
the template strings. They are replaced with user-defined values when SQL
queries are built.
See https://docs.python.org/2/library/string.html#template-strings for more
information.

The used placeholders include (alphabetically ordered):

* column_name e.g. name
* columns e.g. name VARCHAR(50), age INTEGER
* discriminant e.g. WHERE age > 18
* table_name e.g. studentTable
* value e.g. 'gocho'
* values e.g. 'gocho', '19'

Redefining a query is allowed. The above placeholders may be placed
in the overriding query in with a ``$`` preceding them.
For example, in SQLite3, viewing tables requires such a query::

  sqlite3> SELECT name FROM sqlite_master WHERE type = 'table';

When building SQL queries, a **context** is used to derive such values.
A context is simply a dictionary-like object with keys matching the
placeholders in the strings. If a key is not found in the object, a
``MonSQLException`` is raised.

Do NOTE that the common/default SQL template queries defined are biased
to **MySQL** since this library is MySQL-first.
'''


from copy import deepcopy
from string import Template
from .exception import sqlstrException


common_pack = {
  "create_table": Template("CREATE TABLE $table_name ($columns);"),
  "show_tables": Template("SHOW tables;"),
  "truncate_table": Template("TRUNCATE TABLE $table_name;"),
  "drop_table": Template("DROP TABLE $if_exists $table_name;"),
  "show_columns": Template("SHOW COLUMNS FROM $table_name;"),
  "insert_record":Template("INSERT INTO $table_name ($columns) VALUES ($values);"),
  "view_record": Template("SELECT $columns FROM $table_name $discriminant;"),
  "count_records": Template("SELECT COUNT($count) FROM $table_name $discriminant;"),
  "delete_record": Template("DELETE FROM $table_name $discriminant;"),
  "update_record": Template("UPDATE $table_name SET $column_name = $value $discriminant;")
}


class Base:
    '''Base class for all SQL variants'''

    lang_pack = common_pack

    def __init__(self):
        '''Instantiate a language templater'''
        self.__context = {}

    @classmethod
    def get_string(cls, key):
        '''Return a string representation of the template string with {key}
        as its identifier
        '''
        return cls.lang_pack[key].safe_substitute()

    def build(self, dict_key, **context):
        '''Build a valid SQL strings using values from {context}

        context -- (dict) mapping of template params to desired values
        '''
        if context:
            self.__context = context
        try:
            query = lang_pack.get(dict_key)
            return query.substitute(self.__context)
        except ValueError:
            raise sqlstrException("Missing template")
        except KeyError:
            raise sqlstrException("Missing parameter")


def language(cls):
    '''Return the class with its own class variables i.e. variables will not be
    accessed from the base class.
    '''
    cls.lang_pack = deepcopy(common_pack)
    return cls


def update_pack(pack):
    '''Return decorator allowing update of class lang_pack with template
    strings from {pack}'''
    def update_class(cls):
        '''Update class {cls} language pack'''
        for key in pack:
            cls.lang_pack[key] = Template(pack[key])
        return cls
    return update_class

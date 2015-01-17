
# sql string templating

An Abstraction of SQL variants


## Installing

```bash
⇒ git clone https://github.com/GochoMugo/sql-string-templating.git
⇒ cd sql-string-templating
⇒ python setup.py install
```

## Getting Started

```python
import sqlstr

mysql_builder = sqlstr.MySQL()
sqlite3_builder = sqlstr.SQLite3()

print("showing tables in mysql: {}".format(mysql_builder.build("show_tables")))
print("showing tables in sqlite3: {}".format(sqlite3_builder.build("show_tables")))
```


## Contributor's Guide

All SQL variants inherit from the Base class (`sqlstr.Base`).

Sample SQL variant:

```python
from sqlstr import *

blue_sql_pack = {
  "show_tables": "awesome tables come here;"
}

@lang_pack(blue_sql_pack)
@language
class BluSQL(Base):
  pass
```

Ensure to add any appropriate tests in the `test/` directory.


## license

__The MIT License (MIT)__

Copyright (c) 2014 Gocho Mugo <mugo@forfuture.co.ke>

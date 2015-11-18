from modules import *
import os
from random import choice
import sqlite3
from bson.json_util import dumps

sqlite_file = 'quotes_test_db.sqlite'
quotes_table = 'quotes'
saying_field = 'saying'
who_field = 'who'
index_name = 'id'

print("Getting quotes for you ...")
# Get a reference to the SQLiteDB
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
# c.execute('SELECT * FROM {tn}'.\
#     format(tn=quotes_table))
# quotes = c.fetchall()

# print(dumps(quotes))
# {\"text\": \"Waar ik inmiddels behoorlijk zenuwachtig van wordt is het lot van Jip en Janneke.\", \"_id\": {\"$oid\": \"553de9f5c520f468864f98ea\"}, \"who\": \"Erik van Wunnik\"}
# for quote in quotes:
#   print(dumps({'text': quote[1], 'saying': quote[2], 'id': quote[0]}))

c.execute('SELECT * FROM {tn} WHERE {cn}={id}'.
          format(tn=quotes_table, cn=index_name, id=5))

quote = c.fetchone()
print(dumps({'text': quote[1], 'saying': quote[2], 'id': quote[0]}))

# TODO
from sys import *
from cs50 import *
from csv import *

if len(argv) != 2:
    exit(1)

house = argv[1]
db = SQL('sqlite:///students.db')

res = db.execute('SELECT * FROM students WHERE house = ? ORDER BY last, first;', house)

for row in res:
    line = row['first']
    if row['middle']:
        line = ' '.join([line, row['middle']])
    line = ' '.join([line, row['last'] + ", born", str(row['birth'])])
    print(line)

# TODO
from sys import *
from cs50 import *
from csv import *

if len(argv) != 2:
    exit(1)

db = SQL('sqlite:///students.db')

with open(argv[1], 'r') as file:
    reader = DictReader(file)

    for row in reader:
        name, house, birth = row['name'], row['house'], row['birth']
        name = name.split()
        first, middle, last = name[0], None, None
        if len(name) == 3:
            middle, last = name[1], name[2]
        else:
            last = name[1]

        db.execute('INSERT INTO students (first, middle, last, house, birth) VALUES (?,?,?,?,?);', first, middle, last, house, birth)
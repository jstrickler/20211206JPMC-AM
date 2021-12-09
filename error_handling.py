import sqlite3

file_path = 'DATA/wombats.txt'

try:
    with open(file_path) as file_in:
        for line in file_in:
            print(line.rstrip())
# err = FileNotFoundError("message")
except (FileNotFoundError, PermissionError) as err:
    print(err)
    #  log?
    #  exit?
    #  print/pop up message for user?

with open('DATA/breakfast.txt') as file_in:
    all_lines = file_in.read().splitlines()

try:
    print(all_lines[99])
except IndexError as err:
    print(err)

nums = [0, 800, 0, 80, 1000, 32, 2, 255, 400, 5, 5000]

for n in nums:
    try:
        result = 26 / n
    except ZeroDivisionError as err:
        print("Got zero!!")
    else:
        print(result)

conn = None
try:
    conn = sqlite3.connect('mydata/junk/foo.db')
except Exception as err:
    print(err)
    exit()
else:
    pass # access db here
finally:  # whether or not there were exceptions
    print("HELLO FROM finally")
    if conn is not None:
        conn.close()

print("all done")
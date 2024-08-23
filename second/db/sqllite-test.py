import sqlite3

# create a connection to the database
conn = sqlite3.connect('test.db')

# create a cursor object
c = conn.cursor()


# create a table
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

# insert data into the table
c.execute("INSERT INTO users (name, email) VALUES (?,?)", ('John Doe', 'johndoe@example.com'))
c.execute("INSERT INTO users (name, email) VALUES (?,?)", ('Jane Doe', 'janedoe@example.com'))
c.execute("INSERT INTO users (name, email) VALUES (?,?)", ('Bob Smith', 'bobsmith@example.com'))
c.execute("INSERT INTO users (name, email) VALUES (?,?)", ('Alice Johnson', 'alicejohnson@example.com'))


# commit the changes
conn.commit()


# fetch data from the table
c.execute("SELECT * FROM users where name =?", ('John Doe',))
rows = c.fetchall()


# print the data
for row in rows:
    print(row)


# close the cursor
c.close()

# close the connection
conn.close()
import mysql.connector as mysql

# Connect to the database
connection = mysql.connect(
  host="localhost",
  port=3306,
  user="root",
  password="tm12356",
  database="test"
)

cursor = connection.cursor()


# Create a table
cursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))")


# Insert data into the table
cursor.execute("INSERT INTO customers (name, email) VALUES (%s, %s)", ("John Doe", "johndoe@example.com"))
cursor.execute("INSERT INTO customers (name, email) VALUES (%s, %s)", ("Jane Smith", "janesmith@example.com"))
cursor.execute("INSERT INTO customers (name, email) VALUES (%s, %s)", ("Bob Johnson", "bobjohnson@example.com"))
cursor.execute("INSERT INTO customers (name, email) VALUES (%s, %s)", ("Mary Lee", "marylee@example.com"))

connection.commit()
cursor.close()


# Select data from the table
cursor = connection.cursor()
cursor.execute("SELECT * FROM customers")
result = cursor.fetchall()


# Print the result
for row in result:
  print(row)


# close the cursor
cursor.close()
# Close the connection
connection.close()


import sqlite3

def display_data_in_raw_mode(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def display_data_in_parse_mode(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    columns = [description[0] for description in cursor.description]
    rows = cursor.fetchall()
    for row in rows:
        parsed_row = ', '.join(f"{column}: {value}" for column, value in zip(columns, row))
        print(parsed_row)

# Ask for the location of the .db file
db_file_location = input("Enter the location of the .db file: ")

# Ask for the display mode
mode = input("Enter the display mode ('raw' or 'parse'): ")

# Connect to the SQLite database
connection = sqlite3.connect(db_file_location)

# Get the table names from the database
cursor = connection.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_names = [row[0] for row in cursor.fetchall()]

# Check if there are any tables in the database
if not table_names:
    print("No tables found in the database.")
    connection.close()
    exit()

# Display data from all tables
for table_name in table_names:
    print(f"Table: {table_name}")
    if mode == "raw":
        display_data_in_raw_mode(connection, table_name)
    elif mode == "parse":
        display_data_in_parse_mode(connection, table_name)
    print()

# Close the database connection
connection.close()

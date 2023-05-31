# pysqlite3-reader
Displays SQL-DB in RAW or PARSE mode

#############################README#############################

pysqlite3-reader.py - SQLite Database Reader

This script allows you to interact with an SQLite database file (`.db`) using the `pysqlite3` library in Python. It prompts you to enter the location of the `.db` file and then asks for the display mode ('raw' or 'parse'). Afterward, it displays the data from all tables in the selected mode.

#############################README#############################

Usage:
1. Make sure you have Python 3 installed on your system.

2. Install the `pysqlite3` library if you haven't already. You can install it using the following command:
pip install pysqlite3

3. Run the script using the following command:
python3 pysqlite3-reader.py

4. The script will prompt you to enter the location of the `.db` file. Provide the full path to the `.db` file.

5. After entering the file location, the script will ask you to choose the display mode ('raw' or 'parse').
- 'raw' mode: Displays the data from the database as raw rows.
- 'parse' mode: Displays the data from the database in a more human-readable format, with column names and values.

6. The script will then connect to the database, retrieve the table names, and display the data from each table based on the selected mode.

7. Once the data is displayed for all tables, the script will close the database connection.

#############################README#############################

Note:
- If the `.db` file doesn't exist or is not a valid SQLite database, an error will be displayed.
- If there are no tables found in the database, a message will be displayed indicating no tables were found.
- If an invalid display mode is entered, the script will display an error message and terminate.

#############################README#############################

The readme.txt file provides an overview of the script and provides step-by-step instructions on how to use it. It explains the purpose of the script, installation requirements, and usage instructions. It also includes notes on error handling and possible scenarios when interacting with the script.

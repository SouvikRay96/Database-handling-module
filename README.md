# Database-handling-module
It has all the database querry embedded with functions with connectivity in Python

This module has all the functions such as for creating a database and table (if it doesn't exists),
insert data or records in the table, update records of the table, delete records, alter the description of the table, etc etc,.

The python module is working on a user defined database rather than a pre-defined database.

Here we created such a module where we call any function which executes the SQL commands on PYTHON interface.

List of functions:

create_database()
    This function create's a database on the SQL server if it doesn't exists. It has only one parameter that is the database name 
    which is to be given by the user. If it exists then it prints a message to inform the user
del_database()
    This function delete's a database on the SQL server if it exists. It takes only one parameter that is the database name which 
    is to be deleted. If it doesn't exists it prints/display a message to inform the user.
create_table()
    This function create's a table on the specified database by the user if the table doesn't exists. It takes only one parameter
    that is the databse name where the table is to be created, and when the function gets executed it asks for the table name and the 
    field names with their data types from the user.
del_table()
    This function delete's a table if it exists in the specified database by the user. It also takes only one parameter which is the database name from where the table is to be deleted. When the function gets executed it asks for the table name which is to be deleted. If the table does not exists then it prints/display a message to inform the user.
insert_single_record()
    This function helps to insert a single record to the specified table by the user. It takes two parameters : the database name and the table name. It asks the user for each record of the field
    and the procedure how it inserts the record is given with comments in the program itself
insert_multi_records()
    This function helps to insert multiple records to the specified table by the user. It takes two
    parameters : the databse name and the table name. it prompts the user to enter how many number of 
    records do the user wants to insert and then works in the way which is totally explained in program.
del_records()
    This function delete's the selected record by the user from the specified table.
update_records()
    This function updates the field's records as specified by the user according to the condition given by the user. First it prompts the user to enter how many fields do the user wants to update.
    Then as accordingly it takes input of the updated values from the user. Then it ask's for a condition according to which the fields are to be updated. Then it executes the command and finally commits the changes in SQL.
add_single_column()
    This function adds a single column with their datatypes as defined by the user to the table.
add_multi_column()
    This function adds multiple columns with their datatypes as defined by the user to the tbale.
del_column()
    This function delete's one or more columns as specified by the user from the table.
from dataclasses import fields
from msilib.schema import tables
import mysql.connector as sqltor

mydb = sqltor.connect(host = "localhost",user = "root",password = "tojosoumili12",auth_plugin = "mysql_native_password")#establishing connection

mycur = mydb.cursor()#Creating cursor instance

# Creating a Database

def create_database(db_name):
    """This function will let u create your own database on MySQL"""
    mycur.execute("show databases")
    databases = mycur.fetchall() # To fetch all the databases present on the MySQL server
    #This coming if-else codeblock will create a database iff it is not present , otherwise it will print a message
    if (db_name,) not in databases:
        command = "Create database {}".format(db_name)
        mycur.execute(command)
    else:
        print("The database already exists...!!!")

# Deleting a Database

def del_database(db_name):
    """This function is to delete the database the user wants to"""
    mycur.execute("show databases")
    databases = mycur.fetchall() # To fetch all the databases present on the MySQL server
    #This if-else code block will delete the database an user wants to iff it is present, otherwise it will print a message
    if (db_name,) in databases:
        command = "drop database {}".format(db_name)
        mycur.execute(command)
        print("Database deleted successfully...!!!")
    else:
        print("Sorry !!! The database does not exists so the deletion is not possible...")

# Creating a Table

def create_table(db_name):
    """This function is to create a table in the prefered database of the user"""
    table_name = input("Enter the name of the table which u want to create: ")
    mycur.execute("use {}".format(db_name)) # To select the current working database
    mycur.execute("show tables")
    tables = mycur.fetchall() # To fetch all the tables present in the current working database
    # This if-else block will create a table on the database which the user wants to iff it doesn't exists, otherwise will print a message
    if (table_name,) not in tables:
        fields = int(input("How many fields do you want to have in your table: ")) # To enter number of fields to be created
        temp_dict = {} # This dictionary will store the field names with their data types
        for i in range(1,fields + 1):
            field_name = input("Enter the field name: ")
            data_type = input("Enter the data type of the field: ")
            temp_dict[field_name] = data_type # The keys of the dictionary are it's field names and the values are their data types
        parameters = "" # This string will store the field names with their corresponding data types
        c = 0 # This is a counter variable
        # This variable creates a tab that will make python aware of the last field of the table.
        # This is because we don't give a comma after we enter the last field name and the data type.
        for field_name,data_type in temp_dict.items():
            c = c + 1
            if c != fields:
                parameters = parameters + "{} {},".format(field_name,data_type)
            else:
                parameters = parameters + "{} {}".format(field_name,data_type)
        command = "create table {}({})".format(table_name,parameters) # Formatting the command for creating a table in SQL
        mycur.execute(command) # Executing the command to create the table
        print("Table Created successfully...") # Message to display that the table is created succecessfully
    else:
        print("The table already exists..!!!") # Message to display that the table can't be created cz it exists

# Deleting a Table

def del_table(db_name):
    """This function is to delete a table from the preffferred database"""
    table_name = input("Enter the table name which is to be deleted: ")
    mycur.execute("use {}".format(db_name)) # To select the current working database
    mycur.execute("show tables")
    tables = mycur.fetchall() # To fetch all the tables present in the current working database
    #The below if-else block will delete the required table iff it is present in the database, otherwise will print a message
    if (table_name,) in tables:
        mycur.execute("drop table {}".format(table_name))
        print("Table deletion successfull")
    else :
        print("Sorry !!! The table does not exists in the database , so the deletion is not possible...")

# Insertion of Single Record into the table

def insert_single_record(db_name,table_name):
    """This function is to be used to insert a record or a new row in a table
    NOTE : Only one row at a time can be inserted, To enter more rows we need to call the function again"""
    mycur.execute("use {}".format(db_name)) # To select the current working database
    mycur.execute("desc {}".format(table_name)) # To fetch the description of the table viz. field_names and their data_types
    data = mycur.fetchall()
    temp_tuple = tuple() # Creating an empty tuple to store the records to be inserted into the table
    temp_desc = {} # Creating an empty dictionary which will hold the field names as keys and their corresponding datatypes as values
    for i in data:
        temp_desc[i[0]] = i[1] # Storing fieldnames as keys and datatypes as values in the dictionary
    print("Please enter the data/records to the following fields...")
    print()
    for field_name,data_type in temp_desc.items():
        if "int" in data_type:
            rec = int(input("Enter {} : ".format(field_name)))
            temp_tuple = temp_tuple + (rec,) # Taking and storing the records in the tuple which are of integer data type
        elif "char" in data_type:
            rec = input("Enter {} : ".format(field_name))
            temp_tuple = temp_tuple + (rec,) # Taking and storing the records in the tuple which are of string/character data type
    command = "insert into {table_name} values{records}".format(table_name = table_name,records = temp_tuple)
    mycur.execute(command) # Executing the command
    mydb.commit() # Commiting the changes in the specified table
    print()
    print("Record Inserted successfully to the specified table...") # Message to display that insertion done successfully
    print()

# Insertion of multiple records at a time in the table

def insert_multi_records(db_name,table_name):
    """This function is used to enter multiple records in a table
    NOTE : You have to specify the number of records you want to enter"""
    try:
        mycur.execute("use {}".format(db_name)) # To select the current working database
        mycur.execute("desc {}".format(table_name)) # To fetch the description of the table viz. field_names and their data_types
        data = mycur.fetchall()
        rec_list = list()
        temp_tuple = tuple() # Creating an empty tuple to store the records to be inserted into the table
        temp_desc = {} # Creating an empty dictionary which will hold the field names as keys and their corresponding datatypes as values
        for i in data:
            temp_desc[i[0]] = i[1] # Storing fieldnames as keys and datatypes as values in the dictionary
        rec_number = int(input("How many records do you want to enter: "))
        for i in range(1,rec_number + 1):
            print()
            print("Enter data to the fields for record no.{}".format(i))
            print()
            for field_name,data_type in temp_desc.items():
                if "int" in data_type:
                    rec = int(input("Enter {} : ".format(field_name)))
                    temp_tuple = temp_tuple + (rec,) # Taking and storing the records in the tuple which are of integer data type
                elif "char" in data_type:
                    rec = input("Enter {} : ".format(field_name))
                    temp_tuple = temp_tuple + (rec,) # Taking and storing the records in the tuple which are of string/character data type
            rec_list.append(temp_tuple) # Storing the tuples in a list which contains records for multiple rows
            temp_tuple = tuple() # Re-initializing the tuple as empty tuple
        for i in range(0,rec_number):
            command = "insert into {table_name} values{records}".format(table_name = table_name,records = rec_list[i])
            mycur.execute(command) # Executing the command to insert the records in the table
            mydb.commit() # Commiting each record in the table one by one at a time
        print()
        print("The records are inserted SUCCESSFULLY..!!!") # Message to display that insertion done successfully
        print()
    except sqltor.IntegrityError as err:
        print("Error {}".format(err))


# Deleting a record or multiple records or all records from a table

def del_records(db_name,table_name):
    """This function is to delete a record or multiple records that matches the given condition by the user from the mentioned table by the user.
    This function also delete's all the records from the table.
    This is done by giving choices to the user that they want to delete a single record or multiple records based on a condition
    or delete all the records from the table."""
    mycur.execute("use {database_name}".format(database_name = db_name)) # To select the current working database
    print() # Giving the choices to the user
    print("1) Do you want to delete a record or multiple records based on a condition...")
    print("2) Do you want to delete all the records from the mentioned table...")
    print()
    print("NOTE: Please enter a valid choice otherwise error will be shown !!!") # Displaying a warning message
    print()
    ch = int(input("Enter your choice: ")) # Statement to enter the choice by the user
    if ch == 1:
        print("NOTE: You should provide the full condition with the field name...")
        print()
        print("Here are the field names shown below...")
        print() # Block to display all the field names which are present inside the table
        mycur.execute("desc {}".format(table_name))
        data = mycur.fetchall()
        for i in data:
            print(i[0],"  ",end="")
        print()
        condition = input("Enter the conditon based on which the deletion will take place: \n") # Giving the condition by the user
        command = "delete from {} where {}".format(table_name,condition)
        mycur.execute(command) # Executing the command
        mydb.commit() # Commiting changes in SQL
        print()
        print("The deletion of the selected row(s) from the {table_name} based on the condition is successfull...".format(table_name = table_name))
        print() # Printing a message to notify that the process is successfull
    elif ch == 2:
        command = "delete from {}".format(table_name) # Giving the command to delete all the records from the table
        mycur.execute(command) # Executing the command
        mydb.commit() # Commiting changes in SQL
        print()
        print("All the records from the table {table_name} has been deleted...".format(table_name = table_name))
        print() # Printing a message to notify that the process is successfull
        
# Updating a record or multiple records in the table

def update_records(db_name,table_name):
    """This function will update a record or multiple records based on the given condition by the user.
    NOTE: The user should provide the field name of record to be updated..."""
    mycur.execute("use {}".format(db_name))
    mycur.execute("desc {}".format(table_name))
    data = mycur.fetchall()
    temp_dict = {}
    updated_values = ""
    print()
    print("The fields present in the mentioned table by the user are as follows: ")
    print()
    for i in data:
        temp_dict[i[0]] = i[1]
        print(i[0],"  ",end="")
    print()
    fields = int(input("Enter how many fields you want to update: "))
    c = 0
    for i in range(fields):
        print()
        field_name = input("Enter the field name whose record is to be updated: ")
        c = c + 1
        if c != fields:
            if field_name in temp_dict.keys() and "int" in temp_dict[field_name]:
                print()
                field_value = int(input("Enter the updated record of the corresponding {}: ".format(field_name)))
                updated_values += "{field_name}={field_value},".format(field_name = field_name,field_value = field_value)
            elif field_name in temp_dict.keys() and "char" in temp_dict[field_name]:
                print()
                field_value = input("Enter the updated record of the corresponding {}: ".format(field_name))
                updated_values += "{field_name}='{field_value}',".format(field_name = field_name,field_value = field_value)
        else :
            if field_name in temp_dict.keys() and "int" in temp_dict[field_name]:
                print()
                field_value = int(input("Enter the updated record of the corresponding {}: ".format(field_name)))
                updated_values += "{field_name}={field_value}".format(field_name = field_name,field_value = field_value)
            elif field_name in temp_dict.keys() and "char" in temp_dict[field_name]:
                print()
                field_value = input("Enter the updated record of the corresponding {}: ".format(field_name))
                updated_values += "{field_name}='{field_value}'".format(field_name = field_name,field_value = field_value)
    print()
    print("Now provide the condition based on which the updation will take place...")
    print()
    print("These are the field names...")
    for i in data:
        print(i[0],"  ",end="")
    print()
    field_name = input("Enter the field name for the condition: ")
    if field_name in temp_dict.keys() and "int" in temp_dict[field_name]:
        field_value = int(input("Enter the corresponding value for the field: "))
    elif field_name in temp_dict.keys() and "char" in temp_dict[field_name]:
        field_value = input("Enter the corresponding value for the field: ")
    command = "update {table_name} set {values} where {field_name}={field_value}".format(table_name = table_name,values = updated_values,field_name = field_name,field_value = field_value)
    mycur.execute(command)
    mydb.commit()
    print()
    print("The updation done succecsfully...")

# Adding single column to an existing table

def add_single_column(db_name,table_name):
    """This function is used add a column with it's data type to an existing table...
    This function only adds single column to the table. To add more columns we have to again call the function"""
    mycur.execute("use {}".format(db_name)) # To select the current working database
    mycur.execute("show tables") 
    tables = mycur.fetchall() # To fetch all the tables present in the database and storing them in an object called tables
    if (table_name,) in tables: # To check that if the table we try to update exists or not
        col_name = input("Enter the column name which is to be given to the new column: ") # Entering the column name from the user
        col_datatype = input("Enter the data type for the column: ") # Entering the datatype for column from the user
        command = "alter table {table_name} add {col_name} {data_type}".format(table_name = table_name,col_name = col_name,data_type = col_datatype)
        mycur.execute(command) # Executing the command
        mydb.commit() # Commiting changes in SQL
        print()
        print("Addition of column to the table is successfull...") # Message to display that the job is done successfully
        print()
    else:
        print()
        print("The table does not exists in the current working database...") # Message to display that the specified table does not exists
        print()

# Adding multiple columns to an existing table

def add_multi_column(db_name,table_name):
    """This function is used to add multiple columns with iy's datatype to an existing table..."""
    mycur.execute("use {}".format(db_name)) # To select the current working database
    mycur.execute("show tables") 
    tables = mycur.fetchall() # To fetch all the tables present in the database and storing them in an object called tables
    add_command = "" # A string variable which stores all the column names with their data types
    if (table_name,) in tables:
        col_number = int(input("How many number of columns you want to add: ")) # Asking user how many columns he/she wants to enter
        print()
        c = 0
        for i in range(col_number):
            c = c + 1
            col_name = input("Enter the column name which is to be added to the table: ")
            col_datatype = input("Enter the data type for the column: ")
            if c != col_number:
                add_command += "add {col_name} {col_datatype},".format(col_name = col_name,col_datatype = col_datatype)
            else:
                add_command += "add {col_name} {col_datatype}".format(col_name = col_name,col_datatype = col_datatype)
        command = "alter table {table_name} {add_command}".format(table_name = table_name,add_command = add_command)
        mycur.execute(command)
        mydb.commit()
        print()
        print("The columns are added successfully...")
        print()
    else:
        print()
        print("The table does not exists...")
        print()

# Deleting columns from the existing table

def del_columns(db_name,table_name):
    """This function is to delete columns from an existing table.
    The number of columns to be deleted is asked by the program to the user."""
    mycur.execute("use {}".format(db_name)) # To select the current working database
    mycur.execute("show tables")
    tables = mycur.fetchall() # To fetch all the tables in the current working database
    del_command = "" # A string variable which stores all the column names which is/are to be deleted
    if (table_name,) in tables:
        col_number = int(input("How many number of columns do you want to delete: "))
        print() # Prompts the user to enter hoe many number of columns is/are to be deleted
        c = 0 # A counter variable which creates a tab when we enter the last column name
        for i in range(col_number):
            c = c + 1
            col_name = input("Enter the column name which is to be deleted: ")
            if c != col_number:
                del_command += "drop column {column_name},".format(column_name = col_name)
            else :
                del_command += "drop column {col_name}".format(col_name = col_name)
        # Formatting the command for the sql
        command = "alter table {table_name} {del_command}".format(table_name = table_name,del_command = del_command)
        mycur.execute(command) # Execution of the command
        mydb.commit() # Committing changes in SQL
        print()
        print("The deletion of selected columns is successfull...")
        print() # Message to display that the deletion of row is successfull
    else:
        print()
        print("The table does not exists...")
        print() # Message to display that the table does not exists


    

db_name = input("Enter database name: ")
table_name = input("Enter table name: ")
add_multi_column(db_name,table_name)
del_columns(db_name,table_name)



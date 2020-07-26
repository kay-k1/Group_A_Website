#!/bin/env python3

#altered from add_gb_to_database to update the tables, coded by Adam

#import statements
import pymysql
import csv

##########################################################################
#Creates connection to database on server (but only from with in the LAMP!)
#May have to change these if we change the password of the mysql database
connection = pymysql.connect(
    host='localhost',
    user='lampuser',
    password='changeme',
    database='SRP'
)

#creates a cursor object which can then manipulate the database
cursor = connection.cursor()

##########################################################################
#opens file and turns comma separated values into a list of lists for easy access to each element
def format_database(file):

	with open(file) as csv_file:
		reader= csv.reader(csv_file)

		list_list = []
		for row in reader:
			list_list.append(row)
		csv_file.close()
	return list_list


#######################################################################################################################################
#input into the virus table
	#stores return value from above def (a list)
list_list = format_database("date_output.txt")
#print(list_list)
	
	#%s means any string
update_command = "update virus set collection_date = %s where accession = %s"
number = 0
for row in list_list:
	accession = str(row[0])
	collection_date = str(row[1])
	#execute method with update_command and string arguments
	cursor.execute(update_command,(collection_date,accession))
	number = number + 1
	print("row updated in virus table")
	print(number)



#######################################################################################################################################

#commits changes to db and then closes the connection
connection.commit()	

#sql and loop that prints table --> can see changes
table_check= "select * from virus"
cursor.execute(table_check)
results = cursor.fetchall()

for row in results:
    print(row)
connection.close()




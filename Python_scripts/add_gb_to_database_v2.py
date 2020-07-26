#!/bin/env python3

#opens output files produced by the morgan_gb_parsing script and adds them to the various tables in the SRP database, coded by AdamC

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
list_list = format_database("virus_output.txt")
#print(list_list)
	
	#creates a cursor object which can then manipulate the database - moved this to the where we make the connection as i think it may not work if it lies in this loop
	#cursor = connection.cursor()
	
	#%s means any string
insert_command = "insert into virus (accession, location, strain_id, Day, Month, Year) values (%s, %s, %s, %s, %s, %s)"
number = 0
for row in list_list:
	accession = str(row[0])
	location = str(row[1])
	strain_id = str(row[2])
	day = (row[3])
	Day = int(day)
	Month = str(row[4])
	year = (row[5])
	Year = int(year)
	#execute method with insert_command and string arguments
	cursor.execute(insert_command,(accession, location, strain_id, Day, Month, Year))
	number = number + 1
	print("row added to virus table")
	print(number)

#######################################################################################################################################
#input into the protein table
#stores return value from above def (a list)
list_list = format_database("protein_output.txt")
#print(list_list)
	
	#creates a cursor object which can then manipulate the database - moved this to the where we make the connection as i think it may not work if it lies in this loop
	#cursor = connection.cursor()
	
	#%s means any string
insert_command = "insert into protein (protein_id, product, PDB_tag, aa_seq, ntd_seq) values (%s, %s, %s, %s, %s)"

for row in list_list:
	protein_id = str(row[0])
	product = str(row[1])
	PDB_tag = str(row[2])
	aa_seq = str(row[3])
	ntd_seq= str(row[4])
		#execute method with insert_command and string arguments
	cursor.execute(insert_command,(protein_id, product, PDB_tag, aa_seq, ntd_seq))
	print("row added to protein table")


#######################################################################################################################################
#input into the link table
#stores return value from above def (a list)
list_list = format_database("link_db_output.txt")
#print(list_list)
	
	#creates a cursor object which can then manipulate the database - moved this to the where we make the connection as i think it may not work if it lies in this loop
	#cursor = connection.cursor()
	
	#%s means any string
insert_command = "insert into link (accession, protein_id) values (%s, %s)"

for row in list_list:
	accession = str(row[0])
	protein_id = str(row[1])
	#execute method with insert_command and string arguments
	cursor.execute(insert_command,(accession, protein_id))
	print("row added to link table")


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




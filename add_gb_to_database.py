#!/bin/env python3

#script that searches through a directory of genbank files
#it loops through the directory, opening and extracting information for the database

#import statements
import os
from Bio import SeqIO
import re
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

##################################################################################################################################

directory = r'GB_files'
files = os.listdir(directory)
for genbank in files:
	for seq_record in SeqIO.parse("GB_files/"+genbank, "genbank"):
		i = str(seq_record.id)
		f = str(seq_record.features[0])
		s = str(seq_record.seq)
	
	#open file to store useful info - NB used "w" so that it writes over the same file meaning we do not horde redundant files
	seq_rec = open("seq_rec.txt","w")
	
	#RegEx to extract just the useful info from Morgan's code
	collection_date = re.search(r".*collection_date.*'(.*)'",f)
	country = re.search(r".*country.*'(.*)'",f)
	isolate = re.search(r".*isolate.*'(.*)'",f)
	
	#output uses .group() to select useful part of the RegEx object and puts it into a csv text file
	output = i + ", " + str(collection_date.group(1)) + ", " + str(country.group(1)) + ", " + str(isolate.group(1)) + ", " + s
	seq_rec.write(output)
	seq_rec.close()
	print(output)

	#stores return value from above def (a list)
	list_list = format_database("seq_rec.txt")
	print(list_list)
	
	#creates a cursor object which can then manipulate the database - moved this to the where we make the connection as i think it may not work if it lies in this loop
	#cursor = connection.cursor()
	
	#%s means any string
	insert_command = "insert into virus (accession, release_date, location, strain_id) values (%s, %s, %s, %s)"

	for row in list_list:
		accession = str(row[0])
		release_date = str(row[1])
		location = str(row[2])
		strain_id = str(row[3])
		#execute method with insert_command and string arguments
		cursor.execute(insert_command,(accession, release_date, location, strain_id))
		print("row added to table")

#################################################################################################################################
#commits changes to db and then closes the connection
connection.commit()	

#sql and loop that prints table --> can see changes
table_check= "select * from virus"
cursor.execute(table_check)
results = cursor.fetchall()

for row in results:
    print(row)
connection.close()




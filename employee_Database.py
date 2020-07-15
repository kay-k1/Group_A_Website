import pymysql
import csv
##########################################################################
#Creates connection to database on server (but only from with in the LAMP!)
#May have to change these if we change the password of the mysql database
connection = pymysql.connect(
    host='localhost',
    user='lampuser',
    password='changeme',
    database='staff'

)
##########################################################################
#opens file and turns comma separated values into a list of lists for easy access to each element
def format_employee(file):

	with open(file) as csv_file:
		reader= csv.reader(csv_file)

		list_list = []
		for row in reader:
			list_list.append(row)
		csv_file.close()
	return list_list

##########################################################################

#stores return value from above def (a tuple
list_list = format_employee("employee.txt")
print(list_list)

#creates a cursor object which can then manipulate the database
cursor = connection.cursor()

#%s means any string
insert_command = "insert into employee (first_name,last_name, employee_id) values (%s, %s, %s)"

for row in list_list:
	Fname = str(row[0])
	Lname = str(row[1])
	e_id = str(row[2])
	#execute method with insert_command and string arguments
	cursor.execute(insert_command,(Fname,Lname,e_id))
	print("row added to table")

#commits changes to db and then closes the connection
connection.commit()

#sql and loop that prints table --> can see changes
table_check= "select * from employee"
cursor.execute(table_check)
results = cursor.fetchall()

for row in results:
    print(row)
connection.close()

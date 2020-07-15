import os
from Bio import SeqIO



directory = r'GB_files'
files = os.listdir(directory)
for genbank in files:
	print(genbank)
	gb = open("GB_files/"+genbank,"r")
	gb_lines = gb.readlines()
	for line in gb_lines:
		if(line.startswith("DEFINITION")):
			print(line)


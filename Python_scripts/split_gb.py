#!/bin/env python3

#splits the large genbank file downloads into separate files for use, coded by AdamC

import re

with open("sequence1_200.gb") as genbank:
	contents = genbank.readlines()
	#print(contents)


	for line in contents:
	
		accName = re.search(r"^LOCUS\s*(\w*)\s*.*",str(line))
		if accName is not None:
			print(line)
			fileName = accName.group(1)
			print(fileName)
			separate_file = open(fileName+".gb","a")
			#separate_file.write(str(line))
	
		file_end = re.search(r"^(//)",str(line))
		if file_end is not None:
			print(line)
			separate_file.write(str(line))
			#separate_file.close()
	
		else:
			separate_file.write(str(line))

		
		
	

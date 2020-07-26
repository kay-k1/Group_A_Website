#!/bin/env python3

#altered from original morgan_gb_parsing to find the collection date to add to the virus table as originally day month year were added separately, coded by Morgan amendments by AdamC

import os
from Bio import SeqIO
import re

#finding an existing file in a directory: https://www.csestack.org/python-check-if-file-directory-exists/
#deleting existing files: https://www.dummies.com/programming/python/how-to-delete-a-file-in-python/

date_out = open("date_output.txt", "a")

#getting a list of files in a directory: https://www.newbedev.com/
directory = r'GB_files_may30_jun9'
files = os.listdir(directory)
counter = 0
for f in files:
    #Biopython SeqRecord: https://biopython.org/wiki/SeqRecord
    for seq_record in SeqIO.parse(('GB_files_may30_jun9/'+ f), "genbank"):
        i = seq_record.id
        f = seq_record.features
        feat = str(seq_record.features[0])
        for feature in f:
                    
                if (re.search(r".*collection_date.*'(\d{2})-(\w*)-(\d{4})'",feat)):
                    collection_date = re.search(r".*collection_date.*'(\d{2})-(\w*)-(\d{4})'",feat)
                    Day = str(collection_date.group(1))
                    month = str(collection_date.group(2))
                    Year = str(collection_date.group(3))
                    print(month)
                    if(month == 'Jan'):
                        Month = '01'
                    if(month == 'Feb'):
                        Month = '02'
                    if(month == 'Mar'):
                        Month = '03'
                    if(month == 'Apr'):
                        Month = '04'
                    if(month == 'May'):
                        Month = '05'
                    if(month == 'Jun'):
                        Month = '06'
                    if(month == 'Dec'):
                        Month = '12'
                    


                elif (re.search(r".*collection_date.*'(\d{4})-(\d{2})-(\d{2})'",feat)):
                        collection_date = re.search(r".*collection_date.*'(\d{4})-(\d{2})-(\d{2})'",feat)
                        Day = str(collection_date.group(3))
                        Year = str(collection_date.group(1))
                        month = str(collection_date.group(2))
     
                        if(month == 'Jan'):
                            Month = '01'
                        if(month == 'Feb'):
                            Month = '02'
                        if(month == 'Mar'):
                            Month = '03'
                        if(month == 'Apr'):
                            Month = '04'
                        if(month == 'May'):
                            Month = '05'
                        if(month == 'Jun'):
                            Month = '06'
                        if(month == 'Dec'):
                            Month = '12'
                        else: Month = month
                
        date_out.write(i + "," + Year + Month + Day + "\n")
        
        print("Genbank file " + i + " done")
        counter = counter + 1
        print("I have got through " + str(counter) + " genbank files")
date_out.close()

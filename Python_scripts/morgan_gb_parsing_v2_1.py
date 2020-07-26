#!/bin/env python3
import os
from Bio import SeqIO
import re
import requests
#finding an existing file in a directory: https://www.csestack.org/python-check-if-file-directory-exists/
#deleting existing files: https://www.dummies.com/programming/python/how-to-delete-a-file-in-python/
#if (os.path.exists("output.txt")): os.remove("output.txt")
protein_out = open("protein_output.txt", "a")
link_db_out= open("link_db_output.txt", "a")
virus_out=open("virus_output.txt","a")
#getting a list of files in a directory: https://www.newbedev.com/
directory = r'GB_files'
files = os.listdir(directory)
counter = 0
for f in files:
    #Biopython SeqRecord: https://biopython.org/wiki/SeqRecord
    for seq_record in SeqIO.parse(('GB_files/'+ f), "genbank"):
        i = seq_record.id
        f = seq_record.features
        s = str(seq_record.seq)
        d = seq_record.dbxrefs
        feat = str(seq_record.features[0])
        for feature in f:
            #print(feature)
            if (re.search(r"protein_id.*'(.*)'", str(feature))):
                #get the protein id
                match = re.search(r"protein_id.*'(.*)'", str(feature)) 
                protId = match.group(1)
                print(protId)

                #get the protien product
                if (re.search(r"product, Value: \W{2}(\w| |-){1,50}", str(feature))):
                    match = re.search(r"product, Value: \W{2}(\w| |-){1,50}", str(feature))
                    protProd = (match.group())[18:len(str(feature))]
                else: protProd = "null"
    
                #get the PDB tag
                #downloading files using python:https://likegeeks.com/downloading-files-using-python/ 
                #url = ("https://www.ncbi.nlm.nih.gov/protein/" + protId)
                #r = requests.get(url, allow_redirects=True)
                #cont = r.content
                #cont = cont.decode("utf-8")
                #if (re.search(r"PDB: \w{4}", cont)):
                #    match = re.search(r"PDB: \w{4}", cont)
                #    PDBtag = (match.group())[5:9]
                #else: PDBtag = "null"
                PDBtag = "null"

                #get the amino acid sequence
                if (re.search(r"translation, Value: \W{2}\w{1,10000}", str(feature))):
                    match = re.search(r"translation, Value: \W{2}\w{1,10000}", str(feature))
                    sequence = (match.group())[22:len(str(feature))]
                else: sequence = "null"
                
				#get the nucleotide sequence
                m = re.search(r".*location:.*(join.)?\[(\d*):(\d*)\].*(\[(\d*):(\d*)\])", str(feature))
                if m is not None:
                    ntd_sequence = s[int(m.group(2)):int(m.group(6))]
                    #print(ntd_sequence)
                elif (re.search(r".*location:.*(join.)?\[(\d*):(\d*)\]", str(feature))):
                        m = re.search(r".*location:.*\[(\d*):(\d*)\]", str(feature))
                        ntd_sequence = s[int(m.group(1)):int(m.group(2))]
                        #print(ntd_sequence)
                else: ntd_sequence = "null"
                    
                if (re.search(r".*collection_date.*'(\d{2})-(\w*)-(\d{4})'",feat)):
                    collection_date = re.search(r".*collection_date.*'(\d{2})-(\w*)-(\d{4})'",feat)
                    Day = str(collection_date.group(1))
                    Month = str(collection_date.group(2))
                    Year = str(collection_date.group(3))
                elif (re.search(r".*collection_date.*'(\d{4})-(\d{2})-(\d{2})'",feat)):
                        collection_date = re.search(r".*collection_date.*'(\d{4})-(\d{2})-(\d{2})'",feat)
                        Day = str(collection_date.group(3))
                        Year = str(collection_date.group(1))
                        month = str(collection_date.group(2))
                        if(month == '01'):
                            Month = 'Jan'
                        if(month == '02'):
                            Month = 'Feb'
                        if(month == '03'):
                            Month = 'Mar'
                        if(month == '04'):
                            Month = 'Apr'
                        if(month == '05'):
                            Month = 'May'
                        if(month == '06'):
                            Month = 'Jun'
                        if(month == '12'):
                            Month = 'Dec'
                if (re.search(r".*country.*'(.*)'",feat)):
                    m = re.search(r".*country.*'(.*)'",feat)
                    country = str(m.group(1))
                else: country = "null"
                if (re.search(r".*isolate.*'(.*)'",feat)):
                    isolate = re.search(r".*isolate.*'(.*)'",feat)
                if (re.search(r".*strain.*'(.*)'",feat)):
                    isolate = re.search(r".*strain.*'(.*)'",feat)
                protein_out.write(protId + "," + protProd + "," + PDBtag + "," + sequence + "," + ntd_sequence + "\n")
                link_db_out.write(i + "," + protId + "\n")
        virus_out.write(i + "," + country + ", " + str(isolate.group(1)) + "," + Day + "," + Month + "," + Year + "\n")
        print("Genbank file " + i + " done")
        counter = counter + 1
        print("I have got through " + str(counter) + " genbank files")


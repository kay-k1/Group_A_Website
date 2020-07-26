#!/bin/env python3

#altered from original morgan_gb_parsing to find the spike protein amino acid sequence in the genbank file and then to look at position 613 (as counting starts at 0) to note whether it is part of the D614G variant coded by Morgan and amendments by AdamC.

import os
from Bio import SeqIO
import re


#########################################################################################
#if (os.path.exists("output_features.txt")): os.remove("output_features.txt")
#if (os.path.exists("output_genomes.txt")): os.remove("output_genomes.txt")
#if (os.path.exists("output_with.txt")): os.remove("output_with.txt")

#varient_output_features = open("varient_output_features.txt", "a")
#varient_output_genomes = open("varient_output_genomes.txt", "a")
varient_output_with = open("varient_output_with.txt", "a")

#########################################################################################
#remember to change file name here and just below
directory = r'GB_files_may30_jun9'
files = os.listdir(directory)

for f in files:

    for seq_record in SeqIO.parse(('GB_files_may30_jun9/'+ f), "genbank"):
        f = seq_record.features
        i = seq_record.id
        for feature in f:
            spkProd1 = ""
            spkProd2 = ""
            spkNot = ""
            if (re.search(r"protein_id.*'(.*)'", str(feature))):
                #print(feature)

                #get the protein id
                match = re.search(r"protein_id.*'(.*)'", str(feature))
                protId = (match.group(1))
                #print(protId)
			
                #get the protien product
                if (re.search(r"product, Value: \W{2}(\w| |-|:|;){1,50}", str(feature))):
                    match = re.search(r"product, Value: \W{2}(\w| |-|:|;){1,50}", str(feature))
                    protProd = (match.group())[18:len(str(feature))]
                    print(protProd)
                else: protProd = "null"
    

                #get the sequence
                if (re.search(r"translation, Value: \W{2}\w{1,10000}", str(feature))):
                    match = re.search(r"translation, Value: \W{2}\w{1,10000}", str(feature))
                    sequence = (match.group())[22:len(str(feature))]
                    #print(sequence)
                else: sequence = "null"
        
                #get the notes
                if (re.search(r"note, Value: \W{2}(\w| |-|:|;){1,100}", str(feature))):
                    match = re.search(r"note, Value: \W{2}(\w| |-|:|;){1,100}", str(feature))
                    note = (match.group())[15:len(str(feature))]
                    #print(note)
                else: note = "null"

                #get the synonym
                if (re.search(r"gene_synonym, Value: \W{2}(\w| |-|:|;){1,100}", str(feature))):
                    match = re.search(r"note, Value: \W{2}(\w| |-|:|;){1,100}", str(feature))
                    protSyn = (match.group())[15:len(str(feature))]
                    print(protSyn)
                else: protSyn = "null"

				#The different ways groups around the world have described the spike protein in genbank files
                spkProd1 = re.search(r"(S|s)urface (G|g)lycoprotein", protProd)
                spkProd2 = re.search(r"(S|s) protein", protProd)
                spkNot = re.search(r"(S|s)pike", note)
                spkSyn = re.search(r"(S|s)pike", protSyn)
                if spkProd1 or spkProd2 or spkNot or spkSyn:
                    
                    #below coded by AdamC, all the above coded by Morgan
                    str_seq = str(sequence)
                    print(str_seq)
                    seq_len = len(str_seq)
                    if(seq_len>614):
                        aa_614 = str_seq[613]
                        print(aa_614)
                        varient_output_with.write(i + "," + aa_614 + "\n")
    

varient_output_with.close()


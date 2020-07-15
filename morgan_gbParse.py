from Bio import SeqIO
import re



seq_rec = open("seq_rec.txt","w")

for seq_record in SeqIO.parse("sequence.gb", "genbank"):
	i = str(seq_record.id)
	f = str(seq_record.features[0])
	s = str(seq_record.seq)
	#output = str(i) + ", " + (f) + ", " + str(s)
	#seq_rec.write(output)
	#seq_rec.close()

#print(f)
#RegEx to extract just the useful info from Morgan's code
collection_date = re.search(r".*collection_date.*'(.*)'",f)
country = re.search(r".*country.*'(.*)'",f)
isolate = re.search(r".*isolate.*'(.*)'",f)
#print(isolate.group(1))

output = i + ", " + str(collection_date.group(1)) + ", " + str(country.group(1)) + ", " + str(isolate.group(1)) + ", " + s
seq_rec.write(output)
seq_rec.close()
print(output)

#getting 16s rRNA Sequences
from Bio import SeqIO, Entrez,SeqFeature
import sys

#take list of species names and search Genback using
#Entrez to find 16S region


#temporary single term
#eventually, this will run in a loop to take every sepcies name from a text file and find the 16s seq
Entrez.email = "delaneyjosauer@gmail.com.com"
term = '"E.coli"[Organism]'
handle = Entrez.esearch(db="nucleotide", term = term) #searching genbak via Entrez
record = Entrez.read(handle)
idList = record["IdList"] #Id list of entries that match the term

#use the first id list match to search for specific nucleotide sequences
speHandle = Entrez.efetch(db="nucleotide",id = idList[1],rettype = "gb")
speRecord = SeqIO.read(speHandle,"genbank")
print(speRecord)

#For some reason I can't access the 16s rRNA
#I need someone to connect the top chunk of code(or rewrite it) to the bottom
#Both work on their own but not together yet
#feel free to rewrite and delete as needed
#Here is a script that will extract the rRNA seq from genbank file

for genome in speRecord:
for gene in genome.features:
    if gene.type=="rRNA": 
        if 'product' in gene.qualifiers:
            if '16S' in gene.qualifiers['product'][0]:
                start = gene.location.nofuzzy_start
                end = gene.location.nofuzzy_end
                if 'db_xref' in gene.qualifiers:
                    gi=[]
                    gi=str(gene.qualifiers['db_xref'])
                    gi=gi.split(":")[1]
                    gi=gi.split("'")[0]
                    print (">GeneId|%s|16S rRNA|%s\n%s" % (gi,genome.description,genome.seq[start:end]))
                else:
                    print (">GeneId|NoGenID|16S rRNA|%s\n%s" % (genome.description,genome.seq[start:end]))

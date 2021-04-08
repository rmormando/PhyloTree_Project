#getting 16s rRNA Sequences

from Bio import SeqIO, Entrez,SeqFeature
import sys

#take list of species names and search Genback using
#Entrez to find 16S region


#temporary single term
#eventually, this will run in a loop to take every sepcies name from a text file and find the 16s seq
Entrez.email = "rrajagopal@luc.edu"
name = '"E.coli"[Organism]'
handle = Entrez.esearch(db="nucleotide", term = name) #searching genbak via Entrez
record = Entrez.read(handle)
idList = record["IdList"] #Id list of entries that match the term
#print(idList)
#use the first id list match to search for specific nucleotide sequences
speHandle = Entrez.efetch(db="nucleotide",id = idList[1],rettype = "gb", retmode = 'text')
#speRecord = SeqIO.parse(speHandle,"genbank")
#print(speRecord)


#attempting to piece together the upper and bottom chunks of code

#for genome in speRecord:
for record in SeqIO.parse(speHandle,'genbank'):
    for gene in record.features:
        print(gene)
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

        

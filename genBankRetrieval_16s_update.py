#getting 16s rRNA Sequences

from Bio import SeqIO, Entrez,SeqFeature

#take list of species names and search Genback using
#Entrez to find 16S region

#File IO
filename = "C:\\Users\\Delaney\\Desktop\\taxa_names.txt"
file = open(filename, 'r')
speList = file.read().split("\n")
#print(speList[0])

Entrez.email = "rrajagopal@luc.edu" #for entrez search in loop

for name in speList:
    handle = Entrez.esearch(db="nucleotide", term = name) #searching genbak via Entrez
    record = Entrez.read(handle)
    idList = record["IdList"] #Id list of entries that match the term
    #use the first id list match to search for specific nucleotide sequences
    speHandle = Entrez.efetch(db="nucleotide",id = idList[0],rettype = "gb", retmode = 'text')
    speRecord = SeqIO.read(speHandle,"genbank")
    #print(speRecord)

    for gene in speRecord.features:
        if gene.type=="rRNA": 
            if 'product' in gene.qualifiers:
                if '16S' in gene.qualifiers['product'][0]:
                    start = gene.location.nofuzzy_start
                    end = gene.location.nofuzzy_end
                    if 'db_xref' in gene.qualifiers:
                        dbID=str(gene.qualifiers['db_xref'])
                        print(">" + dbID + " name 16S rRNA sequence" + "\n" + str(speRecord.seq[start:end]))
                        break


        

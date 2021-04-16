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

outfile = open("16Sout.txt","w")
log = open("PhyloTreeLog.log","w")

accList = []
for name in speList:
    handle = Entrez.esearch(db="nucleotide", term = name + " AND refseq[filter]") #searching genbank via Entrez and looking for only refseq entries
    record = Entrez.read(handle)
    idList = record["IdList"] #Id list of entries that match the term
    #use the first id list match to search for specific nucleotide sequences
    #add to list to search for 16S sequence later
    temp = (name, idList[0])
    accList.append(temp)

#split finding accession numbers and searching for 16S sequences for easier trouble shooting
for num in accList:
    speHandle = Entrez.efetch(db="nucleotide",id = num[1],rettype = "gb", retmode = 'text')
    speRecord = SeqIO.read(speHandle,"genbank")
    #print(speRecord)
    for gene in speRecord.features:
        if gene.type=="rRNA": 
            if 'product' in gene.qualifiers:
                if '16S' in gene.qualifiers['product'][0]:
                    #print("16S found")
                    log.write(num[0] + " 16S Sequence Found; accession number " + num[1])
                    start = gene.location.nofuzzy_start
                    end = gene.location.nofuzzy_end
                    if 'db_xref' in gene.qualifiers:
                        dbID=str(gene.qualifiers['db_xref'])
                        outfile.write(">" + num[0] + " 16S rRNA sequence" + "\n" + str(speRecord.seq[start:end]) + "\n")
                        break
outfile.close()
log.close()


        

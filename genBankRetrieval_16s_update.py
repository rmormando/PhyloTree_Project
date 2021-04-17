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


for name in speList:
    handle = Entrez.esearch(db="nucleotide", term = name + " AND refseq[filter]") #searching genbank via Entrez and looking for only refseq entries
    record = Entrez.read(handle)
    idList = record["IdList"] #search through each accession number in the list for a 16S sequence

    count = 0 #will stop loop searching for 16S seq in each ID identified
    while count < 1:
        for entry in idList:
            speHandle = Entrez.efetch(db="nucleotide",id = entry,rettype = "gb", retmode = 'text')
            speRecord = SeqIO.read(speHandle,"genbank")
            #print(speRecord)
            for gene in speRecord.features:
                if gene.type=="rRNA":
                    #print("rrna found")
                    if 'product' in gene.qualifiers:
                        if '16S' in gene.qualifiers['product'][0]:
                            #print("16S found")
                            log.write(name + " 16S Sequence Found; accession number " + entry + "\n")
                            print(str(gene.location.extract(speRecord).seq))
                            outfile.write(">" + name + " 16S rRNA sequence" + "\n" + str(gene.location.extract(speRecord).seq) + "\n")
                            count += 1
                if gene.type=="CDS": #sometimes the 16S gene is listed as a CDS and not specifically as rRNA
                    if 'product' in gene.qualifiers:
                        if '16S' in gene.qualifiers['product'][0]:
                            #print("16S found 2")
                            log.write(name + " 16S Sequence Found; accession number " + entry + "\n")
                            print(str(gene.location.extract(speRecord).seq))
                            outfile.write(">" + name + " 16S rRNA sequence" + "\n" + str(gene.location.extract(speRecord).seq) + "\n")
                            count += 1

outfile.close()
log.close()
        

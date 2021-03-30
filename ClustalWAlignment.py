#to run this alignment you need your fasta file and to have
#ClustalW installed. When I wrote this, I installed it on my
#personal computer, but external users will need to install it.
#You also need to install it to run the code.

#ClustalW is a heuristic; it chooses the best alignment at the time
#The alignment is based on pairwaise alignment scores
#It uses a neighboor-joining method to create the global alignment
    #all info taken from ClustalW main website

from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO
import os

file = "C:\\Users\\Delaney\\Downloads\\seqdemp(2).txt"
command = ClustalwCommandline("clustalw2", infile=file)
print(command)

#command created, now you have to run it through the command line
#or call the clustalw executable

#clustalw_exe = r"C:\\Program Files (x86)\\ClustalW2\\clustalw2.exe"
#assert os.path.isfile(clustalw_exe)
#stdout = command()


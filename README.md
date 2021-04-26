# Microbiome Phylogenetic Tree Pipeline
A bioinformatics pipeline for microbiome data analysis using phylogenetic trees.

### To get started, take a look at our design document under the 'Wiki' tab to learn more about the project.


## Introduction
Understanding phylogenetic relationships between different species is crucial for evolutionary studies. Reconstructing the phylogenetic species tree, a branching diagram, is particularly useful in inferring evolutionary relationships. For example, the tree-of-life provides a remarkable view of organizing principles of the biological world. So, the exact species tree to be reconstructed is necessary, but the process of reconstructing the species or gene tree is very tedious.

Here, we developed an easy-to-use pipeline that conveniently and effiecently reconstructs species trees.


## Pipeline Workflow
![Proposed solution PNG]()


## Features
- Inputs only include species names.
- One command line to build trees.
- View trees using ETE.


## Files Included in the Repo
- 16SFastaData.txt
> FASTA format output file of the test data (as a txt file)

- 16Sout.fasta
> FASTA format output file of the test data (as a FASTA file)

- ETE_code.txt
> Code to follow to download the ETE toolkit

- PhyloPipeline
> Main python script for the pipeline

- TreeVisualization
> Python script to visualize the tree

- seqs.afa
> Multiplie sequence alignment output file of the test data (generated by MUSCLE)

- taxa_names.txt
> Test file of taxonomic names

- tree_file
> Newick file of the generated tree from the test data

## Software Tools Required
- Linux/Unix/Mac OS
- Python
  - os: https://docs.python.org/3/library/os.html
  - Biopython (Phlyo): https://biopython.org/wiki/Phylo
- ETE: http://etetoolkit.org/
- plottree: https://github.com/iBiology/plottree
- MUSCLE: http://www.drive5.com/muscle/
- FastTree: http://www.microbesonline.org/fasttree/

## Install
In order to run this code from your working directory, use this git command to clone this repository to your workspace:
```
git clone https://github.com/rmormando/PhyloTree_Project.git
```

Then, change working directories in order to access all files from the cloned repo:
```
cd PhyloTree_Project
```

## Directions

To utilize the pipeline the view tool from the ETE toolkit, MUSCLE, and FastTree must be installed on the local machine or server of your chosing.

Follow the steps outlined in:
```
ETE.txt
```
To download the ETE toolkit software onto your local machine.


**1. Download the sample data set or use your own** 

Make sure it's a text file of taxonomy names separated by line.
```
taxa_names.txt
```
This file is an example input file provided in the repo.


**2. Run through the pipeline** 

Run through the python script with the txt file to access all of the components of the pipeline:
```
python3 PhlyoPipeline.py
```
This single python script file will retrieve the 16s raw reads from NCBI's public database in FASTA format, will create a sequence alignment of the generated FASTA file using MUSCLE, and will then create a tree in Newick format. You can then visualize the newick file on a tree viewer online (we recommend using iTOL), but for your convenience the file named:
```
python3 TreeVisualization.py
```
will create a jpeg of the tree with the branch length using the view tool from the ETE toolkit. 


## Usage

This pipeline has many applications. The Dong and Gao labs at Loyola Universtiy Chicgao challenged us to create a pipeline that will take in a list of taxa names, generated by previous metagenomic analysis of organisms, and develop a way to create a tree from them. There are many previously designed software and tools that account for this solution, however our approach exaggerates the need for efficency while using previously made tools.


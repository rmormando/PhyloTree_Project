# Microbiome Phylogenetic Tree Pipeline
A bioinformatics pipeline for microbiome data analysis using phylogenetic trees.

### To get started, take a look at our design document under the 'Wiki' tab to learn more about the project.


## Introduction
Understanding phylogenetic relationships between different species is crucial for evolutionary studies. Reconstructing the phylogenetic species tree, a branching diagram, is particularly useful in inferring evolutionary relationships. For example, the tree-of-life provides a remarkable view of organizing principles of the biological world. So, the exact species tree to be reconstructed is necessary, but the process of reconstructing the species or gene tree is very tedious.

Here, we developed an easy-to-use pipeline that conveniently and effiecently reconstructs species trees.

## Pipeline Workflow
![Proposed solution PNG](https://github.com/rmormando/PhyloTree_Project/blob/main/updated_workflow.png)

## Features
- Inputs only include species names.
- One command line to build trees.
- View trees using ETE.

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

**1. Download the sample data set or use your own** 
Make sure it's a text file of taxonomy names separated by line.

**2. Obtain the 16S raw reads from NCBI** 
Using the txt file of sample data retrieve the 16s raw reads from NCBI's public database in FASTA format.

Run this line of code with the txt file to retrieve them:
```
[code here]
```

**3. Use the generated FASTA file to generate the tree**
Run this line of code with the FASTA file to generate the tree:
- choose a workflow name (-w)
- choose FASTA target seqeunces (-a for amino acids and -n for nucleotides)
- choose a name for the output tree file (-o)

```
ete3 build -a [fastafile].fasta -w soft_modeltest -o output_tree
```

## Usage

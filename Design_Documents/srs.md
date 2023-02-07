# Software Requirements Specification
## HLA_DNA_Typing
### Laura Davis

1. Introduction
  - Purpose: This tool will produce a list of the HLA alleles that are present in the sample DNA file
  - Scope: Tool uses the IPD-IMGT/HLA database to get a fasta file of all HLA alleles for each HLA gene. Tool must take in user's file of sample DNA sequences and convert fastq and SAM/BAM file to fasta. Then, tool must compare the fasta files and produce a list of alike alleles.
2. Overall Description
  - Functions: Can be used to match people with high numbers of alike HLA alleles; can be used to compare common alleles in different demographics; etc.
  - Users: Researchers or medical personel that have access to a patient's DNA sequencing data in any of the file formats: fasta, fastq, SAM/BAM
  - Constraints: For now, the project is being tested with smaller files -- ex: testing the code with just Class I genes for the HLA dataset; user must have ability to have data in the acceptable formats
3. Requirements
  - Functional: Produce clear list of HLA alleles
  - Nonfunctional: Alignment, bam2fasta, HLA matching

# HLA DNA Typing

Determining the types of HLA alleles that a person has, later will be applied to populations
Eventually could be used to create a reliable bank of donors/recipients

Input: HLA Allele Set in fasta format, DNA sequencing data (WGS) for a person that will be converted into fasta
Output: Set of HLA alleles present in the sample

We will start with chromosome 6 DNA sequence from the reference genome and build the algorithm using these, as well as the HLA reference database for reference.

We will create multiple test sequences from that reference sequence to test many "alleles" and edge cases

The latest status and happy path implementation takes in a test data file initial_test.fna and returns the HLA type, which is A.

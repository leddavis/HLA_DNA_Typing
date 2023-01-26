import pandas as pd


def read_sample_data(file_name, file_type):
    ## fastq file must align to SAM/BAM, then convert to fasta, then be read
    if file_type == "fastq" or file_type == "fq":
        aligned_file = align_sequence(file_name)
        sample_data = convert_aligned_fasta(aligned_file)
        sample_data_seq = read_fasta(sample_data)
    ## SAM/BAM must convert to fasta, then be read
    elif file_type == "sam" or file_type == "bam":
        sample_data = convert_aligned_fasta(file_name)
        sample_data_seq = read_fasta(sample_data)
    ## fasta files get read
    elif file_type == "fasta" or file_type == "fa":
        sample_data = read_fasta(file_name)
    ## Otherwise, ask for new file type
    else:
        print("File is not in acceptable format. Only accepts fasta, fa, fastq, fq, bam, or sam"
    return sample_data_seq

## function to ready fasta file with multiple gene reads
def read_fasta(file_name):
    if '.gz' in file_name:
        file = gunzip.open(file, 'rt')
    else:
        file = open(file, 'rt')     
    id = ''
    sequence = ''
    for line in file:      
        # Read ID
        if line.startswith('>'): 
            id = line[1:]#removes the carrot  
        # Adds the next gene/allele to our sequence
        else:
            sequence += line.strip()
    return sequence

              
def read_HLA_data(HLAs_file):
    HLAs_data = [] ## HLAs_data is a list of the alleles
    ## Read HLA data here, an allele will contain 2 parts: ID and sequence
    ## Create allele class
    return HLAs_data

def match_HLA(sample_data_seq, HLA_data):
    match = False
    ## Compare sample to HLA for present alleles
    ## is HLA_data a subset of sample_data_seq
    return match

def convert_aligned_fasta(aligned_file):
    fasta_file = None
    ## Do conversion here
    return fasta_file

def align_sequence(fastq_file):
    aligned_file = None
    ## Do alignment here (use BowTie, TopHat, etc.)
    return aligned_file

def HLA_DNA_Typing(HLAs_file, sample_file, sample_file_type):
    HLAs_data = read_HLA_data(HLAs_file)
    sample_data_seq = read_sample_data(sample_file, sample_file_type)
    matches = []
    for allele in HLAs_data:
        is_Match = match_HLA(sample_data_seq, allele.sequence)
        if is_Match:
              matches.append(allele.ID)
    return matches
              
              
              
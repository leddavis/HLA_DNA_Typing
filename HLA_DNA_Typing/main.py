import pandas as pd


def read_sample_data(file_name, file_type):
    if file_type == "fastq" or file_type == "fq":
        aligned_file = align_sequence(file_name)
        sample_data = convert_aligned_fasta(aligned_file)
    elif file_type == "sam" or file_type == "bam":
        sample_data = convert_aligned_fasta(file_name)
    elif file_type == "fasta" or file_type == "fa":
        sample_data = None
        ## Read sample data here
    else:
        print("File is not in acceptable format. Only accepts fasta, fa, fastq, fq, bam, or sam"
    return sample_data

def read_HLA_data(HLAs_file):
    HLAs_data = None
    ## Read HLA data here, an allele will contain 2 parts: ID and sequence
    ## Create allele class
    return HLAs_data

def match_HLA(sample_data, HLA_data):
    match = False
    ## Compare sample to HLA for present alleles
    return match

def convert_aligned_fasta(aligned_file):
    fasta_file = None
    ## Do conversion here
    return fasta_file

def align_sequence(fastq_file):
    aligned_file = None
    ## Do alignment here (use BowTie, TopHat, etc.)
    return aligned_file

def HLA_DNA_Typing(HLAs_file, samples_file, sample_file_type):
    HLAs_data = read_HLA_data(HLAs_file)
    sample_data = read_sample_data(sample_file, sample_file_type)
    matches = []
    for allele in HLAs_data:
        is_Match = match_HLA(sample_data, allele.sequence)
        if is_Match:
              matches.append(allele.ID)
    return matches
              
              
              
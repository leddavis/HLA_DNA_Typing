import pandas as pd
import bamnostic as bs
import os

class Sample_Seq:
    def __init__(self, seq_id, sequence, hla_type):
        self.seq_id = seq_id
        self.sequence = sequence
        self.hla_type = hla_type
    
class HLA_Allele:
    def __init__(self, hla_id, allele):
        self.hla_id = hla_id
        self.allele = allele

## Function to get hla_type (HLA gene type) from the gene ID
def get_hla_type(gene_id, gene_id_dict):
    '''
    Finds the HLA type if the gene ID is within the HLA locus
    
    Parameters:
        gene_id (int): an interger value of the gene ID of interest
    
    Returns (str): key - the HLA type corresponding to the gene ID of interest
    '''
    for key, value in HLA_Gene_IDs.items():
        if gene_id == value:
            return key
    return "Key doesn't exist"
    

def read_sample_data(file_name, file_type):
    '''
    Reads the input file and the file type. Depending on the file type, directs the 
    file to the correct function for conversion to fasta and processing of fasta.
    
    Parameters:
        file_name (str): user input file
        file_type (str): user input file type, only accpets fasta, fa, fastq, fq, bam, or sam
    
    Returns (list): sample_data_list - A list of Sample_Seq objects for the given input file
    '''
    ## fastq file must convert to fasta, then be read
    if file_type == "fastq" or file_type == "fq":
        sample_data = fastq_to_fasta(file_name, file_type)
        sample_data_list = read_fasta(sample_data)
    ## SAM/BAM must convert to fasta, then be read
    elif file_type == "sam" or file_type == "bam":
        sample_data = sam_bam_to_fasta(file_name, file_type)
        sample_data_list = read_fasta(sample_data)
    ## fasta files get read
    elif file_type == "fasta" or file_type == "fa":
        sample_data_list = read_fasta(file_name)
    ## Otherwise, ask for new file type
    else:
        print("File is not in acceptable format. Only accepts fasta, fa, fastq, fq, bam, or sam")
    return sample_data_list

              
def read_fasta(file_name):
    '''
    Reads the input file once it is in fasta format, then creates a list of all of the input sequences
    
    Parameters:
        file_name (str): user input file, must be in fasta format
    
    Returns (list): sample_data_list - A list of Sample_Seq objects for the given input file
    '''
    sample_data_list = []
    if '.gz' in file_name:
        file = gzip.open(file_name, 'rt')
    else:
        file = open(file_name, 'rt')       
    seq_id = ''
    sequence = ''
    for line in file:
        if line.startswith('>') and sequence: ## Skip first id, this will be for all future ids
            seq_id = seq_id[1:] ## Removes the carrot
            ## Check if gene is within hla gene list
            id_list = seq_id.split()
            get_gene = id_list[3]
            gene_id = int(gene_id[8, len(gene_id)-1])
            if (gene_id in HLA_Gene_IDs.values()):
                hla_type = get_hla_type(gene_id, HLA_Gene_IDs)
                sample_data_list.append(Sample_Seq(seq_id, sequence, hla_type)) ## Adds sample to list
                seq_id = line.strip() ## All IDs 
                sequence = ''            
        ## Capture first id
        elif line.startswith('>'):  ## First ID
            seq_id = line.strip()           
        ## Capture sequences
        else:
            sequence += line.strip() ## Reads every line of the sequence and makes it 1 string         
    ## This handles the last sequence in the file
    if seq_id and sequence: ## Last sequence
        ## Check if gene is within hla gene list
        seq_id = seq_id[1:] ## Removes the carrot
        id_list = seq_id.split()
        gene_id = id_list[3]
        gene_id = int(gene_id[8, len(gene_id)-1])
        if (gene_id in HLA_Gene_IDs.values()):
            hla_type = get_hla_type(gene_id, HLA_Gene_IDs)
            seq_id = seq_id[1:]
            sample_data_list.append(Sample_Seq(seq_id, sequence, hla_type)) ## Adds last sample to list
    return sample_data_list
              
              
def read_HLA_data(HLAs_file):
    '''
    Reads the HLA alleles data file in fasta format, then connects the HLA types with
    all of their alleles
    
    Parameters:
        HLAs_file (str): HLA alleles data, fasta file from IPD-IMGT/HLA database
    
    Returns (dict): HLAs_data - A dictionary with each HLA type as the keys and their
                    corresponding HLA_Allele objects as the values
    '''
    HLAs_data = {} ## Dictionary with keys as HLA genes and values as the alleles for that gene
    if '.gz' in file_name:
        file = gzip.open(file_name, 'rt')
    else:
        file = open(file_name, 'rt')       
    hla_id = ''
    allele = ''
    for line in file:
        if line.startswith('>') and allele: ## Skip first id, this will be for all future ids
            hla_id = hla_id[1:] ## Removes the carrot
            ## Check which HLA gene it is
            id_list = line.split()
            hla_form = id_list[1]
            get_hla = hla_form.split('*')
            hla_type = get_hla[0]
            if (hla_type in HLA_Gene_IDs.keys()):
                if (hla_type in HLAs_data.keys()):
                    HLAs_data[hla_type].append(HLA_Allele(hla_id, allele))
                else:
                    HLAs_data.setdefault(hla_type, [])
                    HLAs_data[hla_type].append(HLA_Allele(hla_id, allele))
                hla_id = line.strip() ## All allele sequences
                allele = ''            
        ## Capture first id
        elif line.startswith('>'):  ## First allele id
            hla_id = line.strip()           
        ## Capture sequences
        else:
            allele += line.strip() ## Reads every line of the sequence and makes it 1 string         
    ## This handles the last sequence in the file
    if hla_id and allele: ## Last sequence
        hla_id = hla_id[1:]
        id_list = hla_id.split()
        hla_form = id_list[1]
        get_hla = hla_form.split('*')
        hla_type = get_hla[0]
        if (hla_type in HLA_Gene_IDs.keys()):
            if (hla_type in HLAs_data.keys()):
                    HLAs_data[hla_type].append(HLA_Allele(hla_id, allele))
            else:
                HLAs_data.setdefault(hla_type, [])
                HLAs_data[hla_type].append(HLA_Allele(hla_id, allele))
    return HLAs_data

              
def match_HLA(sample_data, HLA_data):
    '''
    Determines if the sample sequence is a match to the HLA allele sequence
    
    Parameters:
        sample_data (str): DNA sequence of the user's input
        HLA_data (str): DNA sequence of the current HLA allele
    
    Returns (bool): match - A boolean value that is true if the two sequences 
                    are equal, and false if not
    '''
    match = False
    ## Compare sample to HLA_Alleles for present alleles
    if sample_data == HLA_data:
        match = true
    else:
        match = false
    return match

## Converts SAM/BAM file to fasta
def sam_bam_to_fasta(aligned_file, file_type):
    ## https://www.biostars.org/p/129763/
    '''
    Converts SAM or BAM files to fasta format conda install -c bioconda bam2fasta
    
    Parameters:
        aligned_file (str): input file in SAM or BAM forma
        file_type (str): input file type, either sam or bam
    
    Returns (file): match - A boolean value that is true if the two sequences 
                    are equal, and false if not
    '''
    fasta_file = None
    if file_type == "sam":
        ## Use samtools view to convert to bam (dependency)
        exit_status = os.system('samtools view -S -b ' + aligned_file + ' > temp.bam')
        temp_bam = open('temp.bam')
        bamtofasta = os.system('samtools bam2fq ' + temp_bam + ' | seqtk seq -A > temp.fa')
        stream = open('temp.fasta')
    else:
        ##Change bam file to fasta file
        bamtofasta = os.system('samtools bam2fq ' + aligned_file + ' | seqtk seq -A > temp.fa')
        stream = open('temp.fasta')
    return stream

## Converts fastq to fasta
## Change this function name DO THIS IN THE WORKFLOW
def fastq_to_fasta(fastq_file):
    '''
    DEPENDENCY: bioconda 
    https://onestopdataanalysis.com/fastq-to-fasta/
    https://janakiev.com/blog/python-shell-commands/
    https://bioconda.github.io/
    '''
    exit_status = os.system('seqtk seq -a ' + fastq_file + ' > temp.fasta')
    ## exit status should be zero try except
    stream = open('temp.fasta')
    return stream

def HLA_DNA_Typing(HLAs_file, sample_file, sample_file_type):
    HLA_Gene_IDs = {'A': 3105, 'B': 3106, 'C': 3107, 'E': 3133, 'F': 3134, \
                   'G': 3135, 'H': 3136, 'J': 3137, 'K': 3138, 'L': 3139, \
                   'N': 267014, 'P': 352963, 'S': 267015, 'T': 352964, 'U': 352965, \
                   'V': 352962, 'W': 352966, 'DMA': 3108, 'DMB': 3109, 'DOA': 3111, \
                   'DPA1': 3113, 'DPA2': 646702, 'DPB1': 3115, 'DPB2': 3116, 'DQA1': 3117, \
                   'DQA2': 3118, 'DQB1': 3119, 'DQB2': 3120, 'DRA': 3122, 'DRB1': 3123, \
                   'DRB2': 3124, 'DRB3': 3125, 'DRB4': 3126, 'DRB5': 3127, 'DRB6': 3128, \
                   'DRB7': 3129, 'DRB8': 3130, 'DRB9': 3132, 'HFE': 3077, 'MICA': 100507436, \
                   'MICB': 4277, 'TAP1': 6890, 'TAP2': 6891}
    HLAs_data = read_HLA_data(HLAs_file) ## Get this to be the file directly from the IGHT-HLA database repository -- For now use downloaded version
    sample_data = read_sample_data(sample_file, sample_file_type, HLA_Gene_IDs) ## List of Sample_Seqs
    matches = []
    for allele in HLAs_data:
        for seq in sample_data:
            is_Match = match_HLA(seq.sequence, allele.sequence) ## check the key that matches hla_type for seq
            if is_Match:
                ## if True, add to master list for output
                matches.append(allele.ID)
    return matches
              
              
              
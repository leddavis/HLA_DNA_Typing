import pandas as pd

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
def get_hla_type(gene_id):
    for key, value in HLA_Gene_IDs.items():
        if gene_id == value:
            return key
    return "Key doesn't exist"

def read_sample_data(file_name, file_type):
    ## fastq file must align to SAM/BAM, then convert to fasta, then be read
    if file_type == "fastq" or file_type == "fq":
        aligned_file = align_sequence(file_name)
        sample_data = convert_aligned_fasta(aligned_file)
        sample_data_list = read_fasta(sample_data, HLA_Gene_IDs)
    ## SAM/BAM must convert to fasta, then be read
    elif file_type == "sam" or file_type == "bam":
        sample_data = convert_aligned_fasta(file_name)
        sample_data_list = read_fasta(sample_data)
    ## fasta files get read
    elif file_type == "fasta" or file_type == "fa":
        sample_data_list = read_fasta(file_name)
    ## Otherwise, ask for new file type
    else:
        print("File is not in acceptable format. Only accepts fasta, fa, fastq, fq, bam, or sam"
    return sample_data_list

              
## Function to read fasta file with multiple gene reads
def read_fasta(file_name):
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
                hla_type = get_hla_type(gene_id)
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
            hla_type = get_hla_type(gene_id)
                seq_id = seq_id[1:]
                sample_data_list.append(Sample_Seq(seq_id, sequence, hla_type)) ## Adds last sample to list
    return sample_data_list
              
              
def read_HLA_data(HLAs_file):
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
                if (hla_type in HLAs_data.keys():
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
            if (hla_type in HLAs_data.keys():
                    HLAs_data[hla_type].append(HLA_Allele(hla_id, allele))
            else:
                HLAs_data.setdefault(hla_type, [])
                HLAs_data[hla_type].append(HLA_Allele(hla_id, allele))
    return HLAs_data

              
def match_HLA(sample_data, HLA_data):
    match = False
    ## Compare sample to HLA_Alleles for present alleles
    if sample_data == HLA_data:
        return true
    else:
        return false

def convert_aligned_fasta(aligned_file):
    fasta_file = None
    ## Do conversion here
    return fasta_file

def align_sequence(fastq_file):
    aligned_file = None
    ## Do alignment here (use BowTie, TopHat, etc.)
    return aligned_file

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
                ## if `e, add to master list for output
                matches.append(allele.ID)
    return matches
              
              
              
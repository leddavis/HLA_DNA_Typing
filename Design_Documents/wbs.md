# WBS
## HLA_DNA_Typing
### Laura Davis

- Activity 1: Set up GitHub repository
- [x] Task 1.1 Set up repo
- [x] Task 1.2 Create description documents
- [x] Task 1.3 Create code structure

- Activity 2: Preprocessing - Read input
- [x] Task 2.1 Define a dictionary variable in main function with the HLA Type as the keys and the Gene ID as the values
- [ ] Task 2.2 Read in the HLA Alleles dataset from the IPD-IMGT/HLA dataset
- [x] Task 2.3 Check which file type user inputs and set up functions to handle each type
- [x] Task 2.4 Check that the input sample sequences are within the HLA genes of interest

- Activity 3: Preprocessing - Convert input data to fasta format (if not already)
- [x] Task 3.1 Check input data file type
- [ ] Task 3.2 Convert fastq files to fasta for simple file comparison
- [ ] Task 3.3 Convert SAM/BAM format to fasta format
      - [x] Task 3.3.1 Determine if file is in SAM or BAM format
      - [ ] Task 3.3.2 Change SAM files to BAM format
            - Dependency: samtools
      - [ ] Task 3.3.3 Change BAM files to fasta
            - Dependency: bam2fasta
 
- Activity 4: Unit Test: Ensure the file is in fasta format before any comparison is done
- [ ] Task 4.1 Create sample data files from the larger files
      -[ ] Task 4.1.1 Create sample_fasta_test1, sample_bam_test1, sample_sam_test1, and sample_fastq_test1: each file type with 1 reference sequence
      -[ ] Task 4.1.2 Run the input data functions and check resulting files for correct fasta format

- Activity 5: Create matching algorithm
- [x] Loop through the HLA list
- [x] Determine if any of the HLA alleles are equal to the sample sequence; if so, add to a list

- Activity 6: Unit Test: Detect the correct allele with only 1 sequence in the input data and only the alleles for that HLA gene
- [ ] Task 6.1 Create sample data files from the larger files
      -[ ] Task 6.1.1 Create sample_data_test2: fasta file with 1 reference sequence for HLA-A
      -[ ] Task 6.1.2 Create hla_data_test2: fasta file with the alleles for gene HLA-A
      -[ ] Task 6.1.3 Run the functions to determine if algorithm produces the correct allele
      
- Activity 7: Implement code to account for many sequences





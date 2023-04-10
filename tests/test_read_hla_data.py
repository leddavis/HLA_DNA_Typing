from HLA_DNA_Typing import main as m

def test_read_hla_small():
    HLA_Gene_IDs = {'A': 3105, 'B': 3106, 'C': 3107, 'E': 3133, 'F': 3134, \
                   'G': 3135, 'H': 3136, 'J': 3137, 'K': 3138, 'L': 3139, \
                   'N': 267014, 'P': 352963, 'S': 267015, 'T': 352964, 'U': 352965, \
                   'V': 352962, 'W': 352966, 'DMA': 3108, 'DMB': 3109, 'DOA': 3111, \
                   'DPA1': 3113, 'DPA2': 646702, 'DPB1': 3115, 'DPB2': 3116, 'DQA1': 3117, \
                   'DQA2': 3118, 'DQB1': 3119, 'DQB2': 3120, 'DRA': 3122, 'DRB1': 3123, \
                   'DRB2': 3124, 'DRB3': 3125, 'DRB4': 3126, 'DRB5': 3127, 'DRB6': 3128, \
                   'DRB7': 3129, 'DRB8': 3130, 'DRB9': 3132, 'HFE': 3077, 'MICA': 100507436, \
                   'MICB': 4277, 'TAP1': 6890, 'TAP2': 6891}
    a1_HLA = m.HLA_Allele('HLA:HLA00001 A*01:01:01:01 3503 bp', 'CAGGAGCAGAGGGGTCAGGGCGAAGTCCCAGGGCCCCAGGCGTGGCTCTCAGGGTCTCAG\
GCCCCGAAGGCGGTGTATGGATTGGGGAGTCCCAGCCTTGGGGATTCCCCAACTCCGCAG\
TTTCTTTTCTCCCTCTCCCAACCTACGTAGGGTCCTTCATCCTGGATACTCACGACGCGG\
ACCCAGTTCTCACTCCCATTGGGTGTCGGGTTTCCAGAGAAGCCAATCAGTGTCGTCGCG\
GTCGCTGTTCTAAAGTCCGCACGCACCCACCGGGACTCAGATTCTCCCCAGACGCCGAGG\
ATGGCCGTCATGGCGCCCCGAACCCTCCTCCTGCTACTCTCGGGGGCCCTGGCCCTGACC\
CAGACCTGGGCGGGTGAGTGCGGGGTCGGGAGGGAAACCGCCTCTGCGGGGAGAAGCAAG\
GGGCCCTCCTGGCGGGGGCGCAGGACCGGGGGAGCCGCGCCGGGAGGAGGGTCGGGCAGG\
TCTCAGCCACTGCTCGCCCCCAGGCTCCCACTCCATGAGGTATTTCTTCACATCCGTGTC\
CCGGCCCGGCCGCGGGGAGCCCCGCTTCATCGCCGTGGGCTACGTGGACGACACGCAGTT\
CGTGCGGTTCGACAGCGACGCCGCGAGCCAGAAGATGGAGCCGCGGGCGCCGTGGATAGA\
GCAGGAGGGGCCGGAGTATTGGGACCAGGAGACACGGAATATGAAGGCCCACTCACAGAC\
TGACCGAGCGAACCTGGGGACCCTGCGCGGCTACTACAACCAGAGCGAGGACGGTGAGTG\
ACCCCGGCCCGGGGCGCAGGTCACGACCCCTCATCCCCCACGGACGGGCCAGGTCGCCCA\
CAGTCTCCGGGTCCGAGATCCACCCCGAAGCCGCGGGACTCCGAGACCCTTGTCCCGGGA\
GAGGCCCAGGCGCCTTTACCCGGTTTCATTTTCAGTTTAGGCCAAAAATCCCCCCGGGTT\
GGTCGGGGCGGGGCGGGGCTCGGGGGACTGGGCTGACCGCGGGGTCGGGGCCAGGTTCTC\
ACACCATCCAGATAATGTATGGCTGCGACGTGGGGCCGGACGGGCGCTTCCTCCGCGGGT\
ACCGGCAGGACGCCTACGACGGCAAGGATTACATCGCCCTGAACGAGGACCTGCGCTCTT\
GGACCGCGGCGGACATGGCAGCTCAGATCACCAAGCGCAAGTGGGAGGCGGTCCATGCGG\
CGGAGCAGCGGAGAGTCTACCTGGAGGGCCGGTGCGTGGACGGGCTCCGCAGATACCTGG\
AGAACGGGAAGGAGACGCTGCAGCGCACGGGTACCAGGGGCCACGGGGCGCCTCCCTGAT\
CGCCTATAGATCTCCCGGGCTGGCCTCCCACAAGGAGGGGAGACAATTGGGACCAACACT\
AGAATATCACCCTCCCTCTGGTCCTGAGGGAGAGGAATCCTCCTGGGTTTCCAGATCCTG\
TACCAGAGAGTGACTCTGAGGTTCCGCCCTGCTCTCTGACACAATTAAGGGATAAAATCT\
CTGAAGGAGTGACGGGAAGACGATCCCTCGAATACTGATGAGTGGTTCCCTTTGACACCG\
GCAGCAGCCTTGGGCCCGTGACTTTTCCTCTCAGGCCTTGTTCTCTGCTTCACACTCAAT\
GTGTGTGGGGGTCTGAGTCCAGCACTTCTGAGTCTCTCAGCCTCCACTCAGGTCAGGACC\
AGAAGTCGCTGTTCCCTTCTCAGGGAATAGAAGATTATCCCAGGTGCCTGTGTCCAGGCT\
GGTGTCTGGGTTCTGTGCTCTCTTCCCCATCCCGGGTGTCCTGTCCATTCTCAAGATGGC\
CACATGCGTGCTGGTGGAGTGTCCCATGACAGATGCAAAATGCCTGAATTTTCTGACTCT\
TCCCGTCAGACCCCCCCAAGACACATATGACCCACCACCCCATCTCTGACCATGAGGCCA\
CCCTGAGGTGCTGGGCCCTGGGCTTCTACCCTGCGGAGATCACACTGACCTGGCAGCGGG\
ATGGGGAGGACCAGACCCAGGACACGGAGCTCGTGGAGACCAGGCCTGCAGGGGATGGAA\
CCTTCCAGAAGTGGGCGGCTGTGGTGGTGCCTTCTGGAGAGGAGCAGAGATACACCTGCC\
ATGTGCAGCATGAGGGTCTGCCCAAGCCCCTCACCCTGAGATGGGGTAAGGAGGGAGATG\
GGGGTGTCATGTCTCTTAGGGAAAGCAGGAGCCTCTCTGGAGACCTTTAGCAGGGTCAGG\
GCCCCTCACCTTCCCCTCTTTTCCCAGAGCTGTCTTCCCAGCCCACCATCCCCATCGTGG\
GCATCATTGCTGGCCTGGTTCTCCTTGGAGCTGTGATCACTGGAGCTGTGGTCGCTGCCG\
TGATGTGGAGGAGGAAGAGCTCAGGTGGAGAAGGGGTGAAGGGTGGGGTCTGAGATTTCT\
TGTCTCACTGAGGGTTCCAAGCCCCAGCTAGAAATGTGCCCTGTCTCATTACTGGGAAGC\
ACCTTCCACAATCATGGGCCGACCCAGCCTGGGCCCTGTGTGCCAGCACTTACTCTTTTG\
TAAAGCACCTGTTAAAATGAAGGACAGATTTATCACCTTGATTACGGCGGTGATGGGACC\
TGATCCCAGCAGTCACAAGTCACAGGGGAAGGTCCCTGAGGACAGACCTCAGGAGGGCTA\
TTGGTCCAGGACCCACACCTGCTTTCTTCATGTTTCCTGATCCCGCCCTGGGTCTGCAGT\
CACACATTTCTGGAAACTTCTCTGGGGTCCAAGACTAGGAGGTTCCTCTAGGACCTTAAG\
GCCCTGGCTCCTTTCTGGTATCTCACAGGACATTTTCTTCCCACAGATAGAAAAGGAGGG\
AGTTACACTCAGGCTGCAAGTAAGTATGAAGGAGGCTGATGCCTGAGGTCCTTGGGATAT\
TGTGTTTGGGAGCCCATGGGGGAGCTCACCCACCCCACAATTCCTCCTCTAGCCACATCT\
TCTGTGGGATCTGACCAGGTTCTGTTTTTGTTCTACCCCAGGCAGTGACAGTGCCCAGGG\
CTCTGATGTGTCTCTCACAGCTTGTAAAGGTGAGAGCTTGGAGGGCCTGATGTGTGTTGG\
GTGTTGGGTGGAACAGTGGACACAGCTGTGCTATGGGGTTTCTTTGCGTTGGATGTATTG\
AGCATGCGATGGGCTGTTTAAGGTGTGACCCCTCACTGTGATGGATATGAATTTGTTCAT\
GAATATTTTTTTCTATAGTGTGAGACAGCTGCCTTGTGTGGGACTGAGAGGCAAGAGTTG\
TTCCTGCCCTTCCCTTTGTGACTTGAAGAACCCTGACTTTGTTTCTGCAAAGGCACCTGC\
ATGTGTCTGTGTTCGTGTAGGCATAATGTGAGGAGGTGGGGAGAGCACCCCACCCCCATG\
TCCACCATGACCCTCTTCCCACGCTGACCTGTGCTCCCTCTCCAATCATCTTTCCTGTTC\
CAGAGAGGTGGGGCTGAGGTGTCTCCATCTCTGTCTCAACTTCATGGTGCACTGAGCTGT\
AACTTCTTCCTTCCCTATTAAAA')
    a2_HLA = m.HLA_Allele('HLA:HLA02169 A*01:01:01:02N 3291 bp', 'GATTGGGGAGTCCCAGCCTTGGGGATTCCCCAACTCCGCAGTTTCTTTTCTCCCTCTCCC\
AACCTACGTAGGGTCCTTCATCCTGGATACTCACGACGCGGACCCAGTTCTCACTCCCAT\
TGGGTGTCGGGTTTCCAGAGAAGCCAATCAGTGTCGTCGCGGTCGCTGTTCTAAAGTCCG\
CACGCACCCACCGGGACTCAGATTCTCCCCAGACGCCGAGGATGGCCGTCATGGCGCCCC\
GAACCCTCCTCCTGCTACTCTCGGGGGCCCTGGCCCTGACCCAGACCTGGGCGGGTGAGT\
GCGGGGTCGGGAGGGAAACCGCCTCTGCGGGGAGAAGCAAGGGGCCCTCCTGGCGGGGGC\
GCAGGACCGGGGGAGCCGCGCCGGGAGGAGGGTCGGGCAGGTCTCAGCCACTGCTCGCCC\
CCAGGCTCCCACTCCATGAGGTATTTCTTCACATCCGTGTCCCGGCCCGGCCGCGGGGAG\
CCCCGCTTCATCGCCGTGGGCTACGTGGACGACACGCAGTTCGTGCGGTTCGACAGCGAC\
GCCGCGAGCCAGAAGATGGAGCCGCGGGCGCCGTGGATAGAGCAGGAGGGGCCGGAGTAT\
TGGGACCAGGAGACACGGAATATGAAGGCCCACTCACAGACTGACCGAGCGAACCTGGGG\
ACCCTGCGCGGCTACTACAACCAGAGCGAGGACGGTGACCCCGGCCCGGGGCGCAGGTCA\
CGACCCCTCATCCCCCACGGACGGGCCAGGTCGCCCACAGTCTCCGGGTCCGAGATCCAC\
CCCGAAGCCGCGGGACTCCGAGACCCTTGTCCCGGGAGAGGCCCAGGCGCCTTTACCCGG\
TTTCATTTTCAGTTTAGGCCAAAAATCCCCCCGGGTTGGTCGGGGCGGGGCGGGGCTCGG\
GGGACTGGGCTGACCGCGGGGTCGGGGCCAGGTTCTCACACCATCCAGATAATGTATGGC\
TGCGACGTGGGGCCGGACGGGCGCTTCCTCCGCGGGTACCGGCAGGACGCCTACGACGGC\
AAGGATTACATCGCCCTGAACGAGGACCTGCGCTCTTGGACCGCGGCGGACATGGCAGCT\
CAGATCACCAAGCGCAAGTGGGAGGCGGTCCATGCGGCGGAGCAGCGGAGAGTCTACCTG\
GAGGGCCGGTGCGTGGACGGGCTCCGCAGATACCTGGAGAACGGGAAGGAGACGCTGCAG\
CGCACGGGTACCAGGGGCCACGGGGCGCCTCCCTGATCGCCTATAGATCTCCCGGGCTGG\
CCTCCCACAAGGAGGGGAGACAATTGGGACCAACACTAGAATATCACCCTCCCTCTGGTC\
CTGAGGGAGAGGAATCCTCCTGGGTTTCCAGATCCTGTACCAGAGAGTGACTCTGAGGTT\
CCGCCCTGCTCTCTGACACAATTAAGGGATAAAATCTCTGAAGGAGTGACGGGAAGACGA\
TCCCTCGAATACTGATGAGTGGTTCCCTTTGACACCGGCAGCAGCCTTGGGCCCGTGACT\
TTTCCTCTCAGGCCTTGTTCTCTGCTTCACACTCAATGTGTGTGGGGGTCTGAGTCCAGC\
ACTTCTGAGTCTCTCAGCCTCCACTCAGGTCAGGACCAGAAGTCGCTGTTCCCTTCTCAG\
GGAATAGAAGATTATCCCAGGTGCCTGTGTCCAGGCTGGTGTCTGGGTTCTGTGCTCTCT\
TCCCCATCCCGGGTGTCCTGTCCATTCTCAAGATGGCCACATGCGTGCTGGTGGAGTGTC\
CCATGACAGATGCAAAATGCCTGAATTTTCTGACTCTTCCCGTCAGACCCCCCCAAGACA\
CATATGACCCACCACCCCATCTCTGACCATGAGGCCACCCTGAGGTGCTGGGCCCTGGGC\
TTCTACCCTGCGGAGATCACACTGACCTGGCAGCGGGATGGGGAGGACCAGACCCAGGAC\
ACGGAGCTCGTGGAGACCAGGCCTGCAGGGGATGGAACCTTCCAGAAGTGGGCGGCTGTG\
GTGGTGCCTTCTGGAGAGGAGCAGAGATACACCTGCCATGTGCAGCATGAGGGTCTGCCC\
AAGCCCCTCACCCTGAGATGGGGTAAGGAGGGAGATGGGGGTGTCATGTCTCTTAGGGAA\
AGCAGGAGCCTCTCTGGAGACCTTTAGCAGGGTCAGGGCCCCTCACCTTCCCCTCTTTTC\
CCAGAGCTGTCTTCCCAGCCCACCATCCCCATCGTGGGCATCATTGCTGGCCTGGTTCTC\
CTTGGAGCTGTGATCACTGGAGCTGTGGTCGCTGCCGTGATGTGGAGGAGGAAGAGCTCA\
GGTGGAGAAGGGGTGAAGGGTGGGGTCTGAGATTTCTTGTCTCACTGAGGGTTCCAAGCC\
CCAGCTAGAAATGTGCCCTGTCTCATTACTGGGAAGCACCTTCCACAATCATGGGCCGAC\
CCAGCCTGGGCCCTGTGTGCCAGCACTTACTCTTTTGTAAAGCACCTGTTAAAATGAAGG\
ACAGATTTATCACCTTGATTACGGCGGTGATGGGACCTGATCCCAGCAGTCACAAGTCAC\
AGGGGAAGGTCCCTGAGGACAGACCTCAGGAGGGCTATTGGTCCAGGACCCACACCTGCT\
TTCTTCATGTTTCCTGATCCCGCCCTGGGTCTGCAGTCACACATTTCTGGAAACTTCTCT\
GGGGTCCAAGACTAGGAGGTTCCTCTAGGACCTTAAGGCCCTGGCTCCTTTCTGGTATCT\
CACAGGACATTTTCTTCCCACAGATAGAAAAGGAGGGAGTTACACTCAGGCTGCAAGTAA\
GTATGAAGGAGGCTGATGCCTGAGGTCCTTGGGATATTGTGTTTGGGAGCCCATGGGGGA\
GCTCACCCACCCCACAATTCCTCCTCTAGCCACATCTTCTGTGGGATCTGACCAGGTTCT\
GTTTTTGTTCTACCCCAGGCAGTGACAGTGCCCAGGGCTCTGATGTGTCTCTCACAGCTT\
GTAAAGGTGAGAGCTTGGAGGGCCTGATGTGTGTTGGGTGTTGGGTGGAACAGTGGACAC\
AGCTGTGCTATGGGGTTTCTTTGCGTTGGATGTATTGAGCATGCGATGGGCTGTTTAAGG\
TGTGACCCCTCACTGTGATGGATATGAATTTGTTCATGAATATTTTTTTCTATAGTGTGA\
GACAGCTGCCTTGTGTGGGACTGAGAGGCAAGAGTTGTTCCTGCCCTTCCCTTTGTGACT\
TGAAGAACCCTGACTTTGTTTCTGCAAAGGCACCTGCATGTGTCTGTGTTCGTGTAGGCA\
TAATGTGAGGAGGTGGGGAGAGCACCCCACCCCCATGTCCACCATGACCCT')
    
    b1_HLA = m.HLA_Allele('HLA:HLA32627 B*44:02:01:71 2712 bp', 'CACCCACCCGGACTCAGAATCTCCTCAGACGCCGAGATGCGGGTCACGGCGCCCCGAACC\
CTCCTCCTGCTGCTCTGGGGGGCAGTGGCCCTGACCGAGACCTGGGCCGGTGAGTGCGGG\
GTCGGGAGGGAAATGGCCTCTGTGGGGAGGAGAGAGGGGACCGCAGGCGGGGGCGCAGGA\
CCCGGGGAGCCGCGCCGGGAGGAGGGTCGGGCGGGTCTCAGCCCCTCCTCGCCCCCAGGC\
TCCCACTCCATGAGGTATTTCTACACCGCCATGTCCCGGCCCGGCCGCGGGGAGCCCCGC\
TTCATCACCGTGGGCTACGTGGACGACACGCTGTTCGTGAGGTTCGACAGCGACGCCACG\
AGTCCGAGGAAGGAGCCGCGGGCGCCATGGATAGAGCAGGAGGGGCCGGAGTATTGGGAC\
CGGGAGACACAGATCTCCAAGACCAACACACAGACTTACCGAGAGAACCTGCGCACCGCG\
CTCCGCTACTACAACCAGAGCGAGGCCGGTGAGTGACCCCGGCCCGGGGCGCAGGTCACG\
ACTCCCCATCCCCCACGTACGGCCCGGGTCGCCCCGAGTCTCCGGGTCCGAGATCCGCCC\
CCGAGGCCGCGGGACCCGCCCAGACCCTCGACCGGCGAGAGCCCCAGGCGCGTTTACCCG\
GTTTCATTTTCAGTTGAGGCCAAAATCCCCGCGGGTTGGTCGGGGCGGGGCGGGGCTCGG\
GGGACGGGGCTGACCGCGGGGCCGGGGCCAGGGTCTCACATCATCCAGAGGATGTACGGC\
TGCGACGTGGGGCCGGACGGGCGCCTCCTCCGCGGGTATGACCAGGACGCCTACGACGGC\
AAGGATTACATCGCCCTGAACGAGGACCTGAGCTCCTGGACCGCGGCGGACACCGCGGCT\
CAGATCACCCAGCGCAAGTGGGAGGCGGCCCGTGTGGCGGAGCAGGACAGAGCCTACCTG\
GAGGGCCTGTGCGTGGAGTCGCTCCGCAGATACCTGGAGAACGGGAAGGAGACGCTGCAG\
CGCGCGGGTACCAGGGGCAGTGGGGAGCCTTCCCCATCTCCTATAGGTCGCCGGGGATGG\
CCTCCCACGAGAAGAGGAGGAAAATGGGATCAGCGCTAGAATGTCGCCCTCCCTTGAATG\
GAGAATGGCATGAGTTTTCCTGAGTTTCCTCTGAGGGCCCCCTCTTCTCTCTAAGACAAT\
TAAGGGATGACGTCTCTGAGGAAATGGAGGGGAAGACAGTCCCTAGAATACTGATCAGGG\
GTCCCCTTTGACCCCTGCAGCAGCCTTGGGAACCGTGACTTTTCCTCTCAGGCCTTGTTC\
TCTGCCTCACACTCAGTGTGTTTGGGGCTCTGATTCCAGCACTTCTGAGTCACTTTACCT\
CCACTCAGATCAGGAGCAGAAGTCCCTGTTCCCCGCTCAGAGACTCGAACTTTCCAATGA\
ATAGGAGATTATCCCAGGTGCCTGCGTCCAGGCTGGTGTCTGGGTTCTGTGCCCCTTCCC\
CACCCCAGGTGTCCTGTCCATTCTCAGGCTGGTCACATGGGTGGTCCTAGGGTGTCCCAT\
GAGAGATGCAAAGCGCCTGAATTTTCTGACTCTTCCCATCAGACCCCCCAAAGACACATG\
TGACCCACCACCCCATCTCTGACCATGAGGTCACCCTGAGGTGCTGGGCCCTGGGCTTCT\
ACCCTGCGGAGATCACACTGACCTGGCAGCGGGATGGCGAGGACCAAACTCAGGACACCG\
AGCTTGTGGAGACCAGACCAGCAGGAGATAGAACCTTCCAGAAGTGGGCAGCTGTGGTGG\
TGCCTTCTGGAGAAGAGCAGAGATACACATGCCATGTACAGCATGAGGGGCTGCCGAAGC\
CCCTCACCCTGAGATGGGGTAAGGAGGGGGATGAGGGGTCATATCTCTTCTCAGGGAAAG\
CAGGAGCCCTTCAGCAGGGTCAGGGCCCCTCATCTTCCCTTCCTTTCCCAGAGCCGTCTT\
CCCAGTCCACCGTCCCCATCGTGGGCATTGTTGCTGGCCTGGCTGTCCTAGCAGTTGTGG\
TCATCGGAGCTGTGGTCGCTGCTGTGATGTGTAGGAGGAAGAGCTCAGGTAGGGAAGGGG\
TGAGGGGTGGGGTCTGGGTTTTCTTGTCCCACTGGGGGTTTCAAGCCCCAGGTAGAAGTG\
TTCCCTGCCTCATTACTGGGAAGCAGCATCCACACAGGGGCTAACGCAGCCTGGGACCCT\
GTGTGCCAGCACTTACTCTTTTGTGCAGCACATGTGACAATGAAGGACGGATGTATCACC\
TTGGTGGTTGTGGTGTTGGGGTCCTGATTCCAGCATTCATGAGTCAGGGGAAGGTCCCTG\
CTAAGGACAGACCTTAGGAGGGCAGTTGGTCCAGGACCCACACTTGCTTTCCTCGTGTTT\
CCTGATCCTGCCTTGGGTCTGTAGTCATACTTCTGGAAATTCCTTTTGGGTCCAAGACGA\
GGAGGTTCCTCTAAGATCTCATGGCCCTGCTTCCTCCCAGTCCCCTCACAGGGCATTTTC\
TTCCCACAGGTGGAAAAGGAGGGAGCTACTCTCAGGCTGCGTGTAAGTGATGGGGGCGGG\
AGTGTGGAGGAGCTCACCCACCCCATAATTCCTCCTGTCCCACGTCTCCTGCGGGCTCTG\
ACCAGGTCCTGTTTTTGTTCTACTCCAGGCAGCGACAGTGCCCAGGGCTCTGATGTGTCT\
CTCACAGCTTGA')
    b2_HLA = m.HLA_Allele('HLA:HLA32918 B*44:02:01:72 2712 bp', 'CACCCACCCGGACTCAGAATCTCCTCAGACGCCGAGATGCGGGTCACGGCGCCCCGAACC\
CTCCTCCTGCTGCTCTGGGGGGCAGTGGCCCTGACCGAGACCTGGGCCGGTGAGTGCGGG\
GTCGGGAGGGAAATGGCCTCTGTGGGGAGGAGAGAGGGGACCGCAGGCGGGGGCGCAGGA\
CCCGGGGAGCCGCGCCGGGAGGAGGGTCGGGCGGGTCTCAGCCCCTCCTCGCCCCCAGGC\
TCCCACTCCATGAGGTATTTCTACACCGCCATGTCCCGGCCCGGCCGCGGGGAGCCCCGC\
TTCATCACCGTGGGCTACGTGGACGACACGCTGTTCGTGAGGTTCGACAGCGACGCCACG\
AGTCCGAGGAAGGAGCCGCGGGCGCCATGGATAGAGCAGGAGGGGCCGGAGTATTGGGAC\
CGGGAGACACAGATCTCCAAGACCAACACACAGACTTACCGAGAGAACCTGCGCACCGCG\
CTCCGCTACTACAACCAGAGCGAGGCCGGTGAGTGACCCCGGCCCGGGGCGCAGGTCACG\
ACTCCCCATCCCCCACGTACGGCCCGGGTCGCCCCGAGTCTCCGGGTCCGAGATCCGCCC\
CCGAGGCCGCGGGACCCGCCCAGACCCTCGACCGGCGAGAGCCCCAGGCGCGTTTACCCG\
GTTTCATTTTCAGTTGAGGCCAAAATCCCCGCGGGTTGGTCGGGGCGGGGCGGGGCTCGG\
GGGACGGGGCTGACCGCGGGGCCGGGGCCAGGGTCTCACATCATCCAGAGGATGTACGGC\
TGCGACGTGGGGCCGGACGGGCGCCTCCTCCGCGGGTATGACCAGGACGCCTACGACGGC\
AAGGATTACATCGCCCTGAACGAGGACCTGAGCTCCTGGACCGCGGCGGACACCGCGGCT\
CAGATCACCCAGCGCAAGTGGGAGGCGGCCCGTGTGGCGGAGCAGGACAGAGCCTACCTG\
GAGGGCCTGTGCGTGGAGTCGCTCCGCAGATACCTGGAGAACGGGAAGGAGACGCTGCAG\
CGCGCGGGTACCAGGGGCAGTGGGGAGCCTTCCCCATCTCCTATAGGTCGCCGGGGATGG\
CCTCCCACGAGAAGAGGAGGAAAATGGGATCAGCGCTAGAATGTCGCCCTCCCTTGAATG\
GAGAATGGCATGAGTTTTCCTGAGTTTCCTCTGAGGGCCCCCTCTTCTCTCTAGGACAAT\
TAAGGGATGACGTCTCTGAGGAAATGGAGGGGAAGACAGTCCCTAGAATACTGATCAGGG\
GTCCCCTTTGACCCCTGCAGCAGCCTTGGGAACCGTGACTTTTCCTCTCAGGCCTTGTTC\
TCTGCCTCACACTCAGTGTGTTTGGGGCTCTGATTCCAGCACTTCTGAGTCACTTTACCT\
CCACTCAGATCAGGAGCAGAAGTCCCTGTTCCCCGCTCAGAGACTCGAACTTTCCAATGA\
ATAGGAGATTATCCCAGGTGCCTGCGTCCAGGCTGGTGTCTGGGTTCTGTGCCCCTTCCC\
CACCCCAGGTGTCCTGTCCATTCTCAGGCTGGTCACATGGGTGGTCCTAGGGTGTCCCAT\
GAGAGATGCAAAGCGCCTGAATTTTCTGACTCTTCCCATCAGACCCCCCAAAGACACATG\
TGACCCACCACCCCATCTCTGACCATGAGGTCACCCTGAGGTGCTGGGCCCTGGGCTTCT\
ACCCTGCGGAGATCACACTGACCTGGCAGCGGGATGGCGAGGACCAAACTCAGGACACCG\
AGCTTGTGGAGACCAGACCAGCAGGAGATAGAACCTTCCAGAAGTGGGCAGCTGTGGTGG\
TGCCTTCTGGAGAAGAGCAGAGATACACATGCCATGTACAGCATGAGGGGCTGCCGAAGC\
CCCTCACCCTGAGATGGGGTAAGGAGGGGGATGAGGGGTCATATCTCTTCTCAGGGAAAG\
CAGGAGCCCTTCAGCAGGGTCAGGGCCCCTCATCTTCCCTTCCTTTCCCAGAGCCGTCTT\
CCCAGTCCACCGTCCCCATCGTGGGCATTGTTGCTGGCCTGGCTGTCCTAGCAGTTGTGG\
TCATCGGAGCTGTGGTCGCTGCTGTGATGTGTAGGAGGAAGAGCTCAGGTAGGGAAGGGG\
TGAGGGGTGGGGTCTGGGTTTTCTTGTCCCACTGGGGGTTTCAAGCCCCAGGTAGAAGTG\
TTCCCTGCCTCATTACTGGGATGCAGCATCCACACAGGGGCTAACGCAGCCTGGGACCCT\
GTGTGCCAGCACTTACTCTTTTGTGCAGCACATGTGACAATGAAGGACGGATGTATCACC\
TTGGTGGTTGTGGTGTTGGGGTCCTGATTCCAGCATTCATGAGTCAGGGGAAGGTCCCTG\
CTAAGGACAGACCTTAGGAGGGCAGTTGGTCCAGGACCCACACTTGCTTTCCTCGTGTTT\
CCTGATCCTGCCTTGGGTCTGTAGTCATACTTCTGGAAATTCCTTTTGGGTCCAAGACGA\
GGAGGTTCCTCTAAGATCTCATGGCCCTGCTTCCTCCCAGTCCCCTCACAGGGCATTTTC\
TTCCCACAGGTGGAAAAGGAGGGAGCTACTCTCAGGCTGCGTGTAAGTGATGGGGGCGGG\
AGTGTGGAGGAGCTCACCCACCCCATAATTCCTCCTGTCCCACGTCTCCTGCGGGCTCTG\
ACCAGGTCCTGTTTTTGTTCTACTCCAGGCAGCGACAGTGCCCAGGGCTCTGATGTGTCT\
CTCACAGCTTGA')
    
    c1_HLA = m.HLA_Allele('HLA:HLA19530 C*06:02:01:15 3903 bp', 'TTATTTTGCTGGATGTAGTTTAATATTACCTGAGGTAAGGTAAGGCAAAGAGTGGGAGGC\
AGGGAGTCCAGTTCAGGGACGGGGATTCCAGGAGAAGTGAAGGGGAAGGGGCTGGGCGCA\
GCCTGGGGGTCTCTCCCTGGTTTCCACAGACAGATCCTTGGCCAGGACTCAGGCACACAG\
TGTGACAAAGATGCTTGGTGTAGGAGAAGAGGGATCAGGACGAAGTCCCAGGTCCCGGGC\
GGGGCTCTCAGGGTCTCAGGCTCCAAGGGCCGTGTCTGCACTGGGGAGGCGCCGCGTTGA\
GGATTCTCCACTCCCCTGAGTTTCACTTCTTCTCCCAACCTGCGTCGGGTCCTTCTTCCT\
GAATACTCATGACGCGTCCCCAATTCCCACTCCCATTGGGTGTCGGGTTCTAGAGAAGCC\
AATCAGCGTCTCCGCAGTCCCGGTTCTAAAGTCCCCAGTCACCCACCCGGACTCGGATTC\
TCCCCAGACGCCGAGATGCGGGTCATGGCGCCCCGAACCCTCATCCTGCTGCTCTCGGGA\
GCCCTGGCCCTGACCGAGACCTGGGCCTGTGAGTGCGGGGTTGGGAGGGAAACGGCCTCT\
GCGGAGAGGAGCGAGGGGCCCGCCCGGCGAGGGCGCAGGACCCGGGGAGCCGCGCAGGGA\
GGTGGGTCGGGCGGGTCTCAGCCCCTCCTCGCCCCCAGGCTCCCACTCCATGAGGTATTT\
CGACACCGCCGTGTCCCGGCCCGGCCGCGGAGAGCCCCGCTTCATCTCAGTGGGCTACGT\
GGACGACACGCAGTTCGTGCGGTTCGACAGCGACGCCGCGAGTCCGAGAGGGGAGCCCCG\
GGCGCCGTGGGTGGAGCAGGAGGGGCCGGAGTATTGGGACCGGGAGACACAGAAGTACAA\
GCGCCAGGCACAGGCTGACCGAGTGAACCTGCGGAAACTGCGCGGCTACTACAACCAGAG\
CGAGGACGGTGAGTGACCCCGGCCCGGGGCGCAGGTCACGACCCCTCCCCATCCCCCACG\
GACGGCCCGGGTCGCCCCGAGTCTCCCGGTCTGAGATCCACCCCGAGGCTGCGGAACCCG\
CCCAGACCCTCGACCGGAGAGAGCCCCAGTCACCTTTACCCGGTTTCATTTTCAGTTTAG\
GCCAAAATCCCCGCGGGTTGGTCGGGGCTGGGGCGGGGCTCGGGGGACGGGGCTGACCAC\
GGGGGCGGGGCCAGGGTCTCACACCCTCCAGTGGATGTATGGCTGCGACCTGGGGCCCGA\
CGGGCGCCTCCTCCGCGGGTATGACCAGTCCGCCTACGACGGCAAGGATTACATCGCCCT\
GAACGAGGACCTGCGCTCCTGGACCGCCGCGGACACGGCGGCTCAGATCACCCAGCGCAA\
GTGGGAGGCGGCCCGTGAGGCGGAGCAGTGGAGAGCCTACCTGGAGGGCACGTGCGTGGA\
GTGGCTCCGCAGATACCTGGAGAACGGGAAGGAGACGCTGCAGCGCGCGGGTACCAGGGG\
CAGTGGGGAGCCTTCCCCATCTCCTATAGGTCGCCGGGGATGGCCTCCCACGAGAAGAGG\
AGGAAAATGGGATCAGCGCTAGAATATCGCCCTCCCTTGAATGGAGAATGGGATGAGTTT\
TCCTGAGTTTCCTCTGAGGGCCCCCTCTGCTCTCTAGGACAATTAAGGGATGAAGTCCTT\
GAGGAAATGGAGGGGAAGACAGTCCCTGGAATACTGATCAGGGGTCCCCTTTGACCACTT\
TGACCACTGCAGCAGCTGTGGTCAGGCTGCTGACCTTTCTCTCAGGCCTTGTTCTCTGCC\
TCACGCTCAATGTGTTTAAAGGTTTGATTCCAGCTTTTCTGAGTCCTTCGGCCTCCACTC\
AGGTCAGGACCAGAAGTCGCTGTTCCTCCCTCAGAGACTAGAACTTTCCAATGAATAGGA\
GATTATCCCAGGTGCCTGTGTCCAGGCTGGCGTCTGGGTTCTGTGCCCCCTTCCCCACCC\
CAGGTGTCCTGTCCATTCTCAGGATGGTCACATGGGCGCTGTTGGAGTGTCGCAAGAGAG\
ATACAAAGTGTCTGAATTTTCTGACTCTTCCCGTCAGAACACCCAAAGACACACGTGACC\
CACCATCCCGTCTCTGACCATGAGGCCACCCTGAGGTGCTGGGCCCTGGGCTTCTACCCT\
GCGGAGATCACACTGACCTGGCAGCGGGATGGCGAGGACCAAACTCAGGACACCGAGCTT\
GTGGAGACCAGGCCAGCAGGAGATGGAACCTTCCAGAAGTGGGCAGCTGTGGTGGTGCCT\
TCTGGAGAAGAGCAGAGATACACGTGCCATGTGCAGCACGAGGGGCTGCCAGAGCCCCTC\
ACCCTGAGATGGGGTAAGGAGGGGGATGAGGGGTCATGTGTCTTCTCAGGGAAAGCAGAA\
GTCCTGGAGCCCTTCAGCCGGGTCAGGGCTGAGGCTTGGGGGTCAGGGCCCCTCACCTTC\
CCCTCCTTTCCCAGAGCCATCTTCCCAGCCCACCATCCCCATCGTGGGCATCGTTGCTGG\
CCTGGCTGTCCTGGCTGTCCTAGCTGTCCTAGGAGCTGTGATGGCTGTTGTGATGTGTAG\
GAGGAAGAGCTCAGGTAGGGAAGGGGTGAGGAGTGGGGTCTGGGTTTTCTTGTCCCACTG\
GGAGTTTCAAGCCCCAGGTAGAAGTGTGCCCCACCTCGTTACTGGAAGCACCATCCACAC\
ATGGGCCATCCCAGCCTGGGACCCTGTGTGCTAGCACTTACTCTGTTGTGAAGCACATGA\
CAATGAAGGACAGATGTATCACCTTGATGATTATGGTGTTGGGGTCCTTGATTCCAGCAT\
TCATGAGTCAGGGGAAGGTCCCTGCTAAGGACAGACCTTAGGAGGGCAGTTGCTCCAGAA\
CCCACAGCTGCTTTCCCCGTGTTTCCTGATCCTGCCCTGGGTCTGCAGTCATAGTTCTGG\
AAACTTCTCTTGGGTCCAAGACTAGGAGGTTCCCCTAAGATCGCATGGCCCTGCCTCCTC\
CCTGTCCCCTCACAGGGCATTTTCTTCCCACAGGTGGAAAAGGAGGGAGCTGCTCTCAGG\
CTGCGTGTAAGTGATGGCGGTGGGCGTGTGGAGGAGCTCACCCACCCCATAATTCCTCTT\
GTCCCACATCTCCTGCGGGCTCTGACCAGGTCTTTTTTTTTGTTCTACCCCAGCCAGCAA\
CAGTGCCCAGGGCTCTGATGAGTCTCTCATCGCTTGTAAAGGTGAGATTCTGGGGAGCTG\
AAGTGGTCTGGGGTGGGGCAGAGGGAAAAGGCCTAGGTAATGGGGATCCTTTGATTGGGA\
CGTTTCGAATGTGTGGTGAGCTGTTCAGAGTGTCATCACTTACCATGACTGACCTGAATT\
TGTTCATGACTATTGTGTTCTGTAGCCTGAGACAGCTGCCTGTGTGGGACTGAGATGCAG\
GATTTCTTCACACCTCTCCTTTGTGACTTCAAGAGCCTCTGGCATCTCTTTCTGCAAAGG\
CATCTGAATGTGTCTGCGTTCCTGTTAGCATAATGTGAGGAGGTGGAGAGACAGCCCACC\
CCCGTGTCCACCGTGACCCCTGTCCCCACACTGACCTGTGTTCCCTCCCCGATCATCTTT\
CCTGTTCCAGAGAAGTGGGCTGGATGTCTCCATCTCTGTCTCAACTTTACGTGTACTGAG\
CTGCAACTTCTTACTTCCCTACTGAAAATAAGAATCTGAATATAAATTTGTTTTCTCAAA\
TATTTGCTATGAGAGGTTGATGGATTAATTAAATAAGTCAATTCCTGGAAGTTGAGAGAG\
CAAATAAAGACCTGAGAACCTTCCAGAATCCGCATGTTCGCTGTGCTGAGTCTGTTGCAG\
GTGGGGGTGGGGAAGGCTGTGAGGAGACGAGTGTGGACGGGGCCTGTGCCTAGTTGCTGT\
TCA')
    c2_HLA = m.HLA_Allele('HLA:HLA20861 C*06:02:01:16 3903 bp', 'TTATTTTGCTGGATGTAGTTTAATATTACCTGAGGTAAGGTAAGGCAAAGAGTGGGAGGC\
AGGGAGTCCAGTTCAGGGACGGGGATTCCAGGAGAAGTGAAGGGGAAGGGGCTGGGCGCA\
GCCTGGGGGTCTCTCCCTGGTTTCCACAGACAGATCCTTGGCCAGGACTCAGGCACACAG\
TGTGACAAAGATGCTTGGTGTAGGAGAAGAGGGATCAGGACGAAGTCCCAGGTCCCGGGC\
GGGGCTCTCAGGGTCTCAGGCTCCAAGGGCCGTGTCTGCACTGGGGAGGCGCCGCGTTGA\
GGATTCTCCACTCCCCTGAGTTTCACTTCTTCTCCCAACCTGCGTCGGGTCCTTCTTCCT\
GAATACTCATGACGCGTCCCCAATTCCCACTCCCATTGGGTGTCGGGTTCTAGAGAAGCC\
AATCAGCGTCTCCGCAGTCCCGGTTCTAAAGTCCCCAGTCACCCACCCGGACTCGGATTC\
TCCCCAGACGCCGAGATGCGGGTCATGGCGCCCCGAACCCTCATCCTGCTGCTCTCGGGA\
GCCCTGGCCCTGACCGAGACCTGGGCCTGTGAGTGCGGGGTTGGGAGGGAAACGGCCTCT\
GCGGAGAGGAGCGAGGGGCCCGCCCGGCGAGGGCGCAGGACCCGGGGAGCCGCGCAGGGA\
GGAGGGTCGGGCGGGTCTCAGCCCCTCCTCGCCCCCAGGCTCCCACTCCATGAGGTATTT\
CGACACCGCCGTGTCCCGGCCCGGCCGCGGAGAGCCCCGCTTCATCTCAGTGGGCTACGT\
GGACGACACGCAGTTCGTGCGGTTCGACAGCGACGCCGCGAGTCCGAGAGGGGAGCCCCG\
GGCGCCGTGGGTGGAGCAGGAGGGGCCGGAGTATTGGGACCGGGAGACACAGAAGTACAA\
GCGCCAGGCACAGGCTGACCGAGTGAACCTGCGGAAACTGCGCGGCTACTACAACCAGAG\
CGAGGACGGTGAGTGACCCCGGCCCGGGGCGCAAGTCACGACCCCTCCCCATCCCCCACG\
GACGGCCCGGGTCGCCCCGAGTCTCCCGGTCTGAGATCCACCCCGAGGCTGCGGAACCCG\
CCCAGACCCTCGACCGGAGAGAGCCCCAGTCACCTTTACCCGGTTTCATTTTCAGTTTAG\
GCCAAAATCCCCGCGGGTTGGTCGGGGCTGGGGCGGGGCTCGGGGGACGGGGCTGACCAC\
GGGGGCGGGGCCAGGGTCTCACACCCTCCAGTGGATGTATGGCTGCGACCTGGGGCCCGA\
CGGGCGCCTCCTCCGCGGGTATGACCAGTCCGCCTACGACGGCAAGGATTACATCGCCCT\
GAACGAGGACCTGCGCTCCTGGACCGCCGCGGACACGGCGGCTCAGATCACCCAGCGCAA\
GTGGGAGGCGGCCCGTGAGGCGGAGCAGTGGAGAGCCTACCTGGAGGGCACGTGCGTGGA\
GTGGCTCCGCAGATACCTGGAGAACGGGAAGGAGACGCTGCAGCGCGCGGGTACCAGGGG\
CAGTGGGGAGCCTTCCCCATCTCCTGTAGATCTCCCGGGATGGCCTCCCACGAGGAGGGG\
AGGAAAATGGGATCAGCGCTAGAATATCGCCCTCCCTTGAATGGAGAATGGGATGAGTTT\
TCCTGAGTTTCCTCTGAGGGCCCCCTCTGCTCTCTAGGACAATTAAGGGATGAAGTCCTT\
GAGGAAATGGAGGGGAAGACAGTCCCTGGAATACTGATCAGGGGTCCCCTTTGACCACTT\
TGACCACTGCAGCAGCTGTGGTCAGGCTGCTGACCTTTCTCTCAGGCCTTGTTCTCTGCC\
TCACGCTCAATGTGTTTAAAGGTTTGATTCCAGCTTTTCTGAGTCCTTCGGCCTCCACTC\
AGGTCAGGACCAGAAGTCGCTGTTCCTCCCTCAGAGACTAGAACTTTCCAATGAATAGGA\
GATTATCCCAGGTGCCTGTGTCCAGGCTGGCGTCTGGGTTCTGTGCCCCCTTCCCCACCC\
CAGGTGTCCTGTCCATTCTCAGGATGGTCACATGGGCGCTGTTGGAGTGTCGCAAGAGAG\
ATACAAAGTGTCTGAATTTTCTGACTCTTCCCGTCAGAACACCCAAAGACACACGTGACC\
CACCATCCCGTCTCTGACCATGAGGCCACCCTGAGGTGCTGGGCCCTGGGCTTCTACCCT\
GCGGAGATCACACTGACCTGGCAGCGGGATGGCGAGGACCAAACTCAGGACACCGAGCTT\
GTGGAGACCAGGCCAGCAGGAGATGGAACCTTCCAGAAGTGGGCAGCTGTGGTGGTGCCT\
TCTGGAGAAGAGCAGAGATACACGTGCCATGTGCAGCACGAGGGGCTGCCAGAGCCCCTC\
ACCCTGAGATGGGGTAAGGAGGGGGATGAGGGGTCATGTGTCTTCTCAGGGAAAGCAGAA\
GTCCTGGAGCCCTTCAGCCGGGTCAGGGCTGAGGCTTGGGGGTCAGGGCCCCTCACCTTC\
CCCTCCTTTCCCAGAGCCATCTTCCCAGCCCACCATCCCCATCGTGGGCATCGTTGCTGG\
CCTGGCTGTCCTGGCTGTCCTAGCTGTCCTAGGAGCTGTGATGGCTGTTGTGATGTGTAG\
GAGGAAGAGCTCAGGTAGGGAAGGGGTGAGGAGTGGGGTCTGGGTTTTCTTGTCCCACTG\
GGAGTTTCAAGCCCCAGGTAGAAGTGTGCCCCACCTCGTTACTGGAAGCACCATCCACAC\
ATGGGCCATCCCAGCCTGGGACCCTGTGTGCTAGCACTTACTCTGTTGTGAAGCACATGA\
CAATGAAGGACAGATGTATCACCTTGATGATTATGGTGTTGGGGTCCTTGATTCCAGCAT\
TCATGAGTCAGGGGAAGGTCCCTGCTAAGGACAGACCTTAGGAGGGCAGTTGCTCCAGAA\
CCCACAGCTGCTTTCCCCGTGTTTCCTGATCCTGCCCTGGGTCTGCAGTCATAGTTCTGG\
AAACTTCTCTTGGGTCCAAGACTAGGAGGTTCCCCTAAGATCGCATGGCCCTGCCTCCTC\
CCTGTCCCCTCACAGGGCATTTTCTTCCCACAGGTGGAAAAGGAGGGAGCTGCTCTCAGG\
CTGCGTGTAAGTGATGGCGGTGGGCGTGTGGAGGAGCTCACCCACCCCATAATTCCTCTT\
GTCCCACATCTCCTGCGGGCTCTGACCAGGTCTTTTTTTTTGTTCTACCCCAGCCAGCAA\
CAGTGCCCAGGGCTCTGATGAGTCTCTCATCGCTTGTAAAGGTGAGATTCTGGGGAGCTG\
AAGTGGTCTGGGGTGGGGCAGAGGGAAAAGGCCTAGGTAATGGGGATCCTTTGATTGGGA\
CGTTTCGAATGTGTGGTGAGCTGTTCAGAGTGTCATCACTTACCATGACTGACCTGAATT\
TGTTCATGACTATTGTGTTCTGTAGCCTGAGACAGCTGCCTGTGTGGGACTGAGATGCAG\
GATTTCTTCACACCTCTCCTTTGTGACTTCAAGAGCCTCTGGCATCTCTTTCTGCAAAGG\
CATCTGAATGTGTCTGCGTTCCTGTTAGCATAATGTGAGGAGGTGGAGAGACAGCCCACC\
CCCGTGTCCACCGTGACCCCTGTCCCCACACTGACCTGTGTTCCCTCCCCGATCATCTTT\
CCTGTTCCAGAGAAGTGGGCTGGATGTCTCCATCTCTGTCTCAACTTTACGTGTACTGAG\
CTGCAACTTCTTACTTCCCTACTGAAAATAAGAATCTGAATATAAATTTGTTTTCTCAAA\
TATTTGCTATGAGAGGTTGATGGATTAATTAAATAAGTCAATTCCTGGAAGTTGAGAGAG\
CAAATAAAGACCTGAGAACCTTCCAGAATCCGCATGTTCGCTGTGCTGAGTCTGTTGCAG\
GTGGGGGTGGGGAAGGCTGTGAGGAGACGAGTGTGGACGGGGCCTGTGCCTAGTTGCTGT\
TCA')
    hla_dict = {'A': [a1_HLA, a2_HLA], 'B': [b1_HLA, b2_HLA], 'C': [c1_HLA, c2_HLA]}
    file = 'tests/Test_Data/initial_hla_tests.fasta'
    test_hla_read = m.read_HLA_data(file, HLA_Gene_IDs)
    test_id_list = []
    test_allele_list = []
    for key in test_hla_read.keys():
        for i in range(0, len(test_hla_read[key])):
            test_id_list.append(test_hla_read[key][i].hla_id)
            test_allele_list.append(test_hla_read[key][i].allele)
    check_id_list = []
    check_allele_list = []
    for key in hla_dict.keys():
        for i in range(0, len(hla_dict[key])):
            check_id_list.append(hla_dict[key][i].hla_id)
            check_allele_list.append(hla_dict[key][i].allele)
    len_of_lists = len(check_id_list)
    if len_of_lists == len(test_id_list):
        for i in range(0, len_of_lists):
            assert test_id_list[i] == check_id_list[i]
            assert test_allele_list[i] == check_allele_list[i]
    else:
        assert FALSE
    
        ##assert test_hla_read[i].allele == hla_dict[i].allele
    ##assert test_hla_read == hla_dict
    ##for i in range(0, len(test_hla_read)):
        ##print(test_hla_read[i])
        ##print(test_hla_read[i].hla_id)
        ##print(hla_dict[i].hla_id)
        ##assert test_hla_read[i].hla_id == hla_dict[i].hla_id
        ##assert test_hla_read[i].allele == hla_dict[i].allele
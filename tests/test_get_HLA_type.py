from HLA_DNA_Typing import main as m

def test_get_HLA_type_a():
    HLA_Gene_IDs = {'A': 3105, 'B': 3106, 'C': 3107, 'E': 3133, 'F': 3134, \
                   'G': 3135, 'H': 3136, 'J': 3137, 'K': 3138, 'L': 3139, \
                   'N': 267014, 'P': 352963, 'S': 267015, 'T': 352964, 'U': 352965, \
                   'V': 352962, 'W': 352966, 'DMA': 3108, 'DMB': 3109, 'DOA': 3111, \
                   'DPA1': 3113, 'DPA2': 646702, 'DPB1': 3115, 'DPB2': 3116, 'DQA1': 3117, \
                   'DQA2': 3118, 'DQB1': 3119, 'DQB2': 3120, 'DRA': 3122, 'DRB1': 3123, \
                   'DRB2': 3124, 'DRB3': 3125, 'DRB4': 3126, 'DRB5': 3127, 'DRB6': 3128, \
                   'DRB7': 3129, 'DRB8': 3130, 'DRB9': 3132, 'HFE': 3077, 'MICA': 100507436, \
                   'MICB': 4277, 'TAP1': 6890, 'TAP2': 6891}
    gene_id = 3105
    #expected result is gene A
    expected_key = "A"
    key = m.get_hla_type(gene_id, HLA_Gene_IDs)
    assert key == expected_key, "The HLA type is " + expected_key + ", not " + key

def test_get_HLA_type_b():
    HLA_Gene_IDs = {'A': 3105, 'B': 3106, 'C': 3107, 'E': 3133, 'F': 3134, \
                   'G': 3135, 'H': 3136, 'J': 3137, 'K': 3138, 'L': 3139, \
                   'N': 267014, 'P': 352963, 'S': 267015, 'T': 352964, 'U': 352965, \
                   'V': 352962, 'W': 352966, 'DMA': 3108, 'DMB': 3109, 'DOA': 3111, \
                   'DPA1': 3113, 'DPA2': 646702, 'DPB1': 3115, 'DPB2': 3116, 'DQA1': 3117, \
                   'DQA2': 3118, 'DQB1': 3119, 'DQB2': 3120, 'DRA': 3122, 'DRB1': 3123, \
                   'DRB2': 3124, 'DRB3': 3125, 'DRB4': 3126, 'DRB5': 3127, 'DRB6': 3128, \
                   'DRB7': 3129, 'DRB8': 3130, 'DRB9': 3132, 'HFE': 3077, 'MICA': 100507436, \
                   'MICB': 4277, 'TAP1': 6890, 'TAP2': 6891}
    gene_id = 3106
    #expected result is gene B
    expected_key = "B"
    key = m.get_hla_type(gene_id, HLA_Gene_IDs)
    assert key == expected_key, "The HLA type is " + expected_key + ", not " + key

def test_get_HLA_type_non():
    HLA_Gene_IDs = {'A': 3105, 'B': 3106, 'C': 3107, 'E': 3133, 'F': 3134, \
                   'G': 3135, 'H': 3136, 'J': 3137, 'K': 3138, 'L': 3139, \
                   'N': 267014, 'P': 352963, 'S': 267015, 'T': 352964, 'U': 352965, \
                   'V': 352962, 'W': 352966, 'DMA': 3108, 'DMB': 3109, 'DOA': 3111, \
                   'DPA1': 3113, 'DPA2': 646702, 'DPB1': 3115, 'DPB2': 3116, 'DQA1': 3117, \
                   'DQA2': 3118, 'DQB1': 3119, 'DQB2': 3120, 'DRA': 3122, 'DRB1': 3123, \
                   'DRB2': 3124, 'DRB3': 3125, 'DRB4': 3126, 'DRB5': 3127, 'DRB6': 3128, \
                   'DRB7': 3129, 'DRB8': 3130, 'DRB9': 3132, 'HFE': 3077, 'MICA': 100507436, \
                   'MICB': 4277, 'TAP1': 6890, 'TAP2': 6891}
    gene_id = 68904576
    #expected result is gene DNE
    expected_key = "Key doesn't exist"
    key = m.get_hla_type(gene_id, HLA_Gene_IDs)
    assert key == expected_key, "The HLA type does not exist "
from HLA_DNA_Typing import main as m

def test_get_HLA_type_a():
    gene_id = 3105
    #expected result is gene lhlkah
    expected_key = "A"
    key = m.get_hla_type(gene_id)
    assert key == expected_key, "The HLA type is " + expected_key + ", not " + key

def test_get_HLA_type_b():
    gene_id = 3106
    #expected result is gene lhlkah
    expected_key = "B"
    key = m.get_hla_type(gene_id)
    assert key == expected_key, "The HLA type is " + expected_key + ", not " + key

def test_get_HLA_type_b():
    gene_id = 68904576
    #expected result is gene lhlkah
    expected_key = "Key doesn't exist"
    key = m.get_hla_type(gene_id)
    assert key == expected_key, "The HLA type does not exist "
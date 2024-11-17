def mrna(protein):
    codons = {
        'F': ['UUU', 'UUC'],
        'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
        'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
        'Y': ['UAU', 'UAC'],
        '*': ['UAA', 'UAG', 'UGA'],  # Stop codon
        'C': ['UGU', 'UGC'],
        'W': ['UGG'],
        'P': ['CCU', 'CCC', 'CCA', 'CCG'],
        'H': ['CAU', 'CAC'],
        'Q': ['CAA', 'CAG'],
        'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
        'V': ['GUU', 'GUC', 'GUA', 'GUG'],
        'A': ['GCU', 'GCC', 'GCA', 'GCG'],
        'D': ['GAU', 'GAC'],
        'E': ['GAA', 'GAG'],
        'G': ['GGU', 'GGC', 'GGA', 'GGG'],
        'I': ['AUU', 'AUC', 'AUA'],
        'M': ['AUG'],  # Start codon
        'T': ['ACU', 'ACC', 'ACA', 'ACG'],
        'N': ['AAU', 'AAC'],
        'K': ['AAA', 'AAG']
    }
    number = 1

    for aa in protein:
        number *= len(codons[aa])
    number *= len(codons["*"])
    return number % 1000000

protein_string = "MA"
result = mrna(protein_string)
print(result)  
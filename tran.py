def transition_transversion_ratio(s1, s2):
    transitions = 0
    transversions = 0

    purines = {'A', 'G'}
    pyrimidines = {'C', 'T'}

    for base1, base2 in zip(s1, s2):
        if base1 != base2:
            if (base1 in purines and base2 in purines) or (base1 in pyrimidines and base2 in pyrimidines):
                transitions += 1
            else:
                transversions += 1

    if transversions == 0:  
        return float('inf') 
    return transitions / transversions

s1 = '''GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT'''
s2 = '''TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT'''

ratio = transition_transversion_ratio(s1, s2)
print(ratio)
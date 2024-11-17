import numpy as np

fasta_data = '''>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT'''

seq_name, seq_string = [], []
current_sequence = ""

for line in fasta_data.splitlines():
    if line.startswith(">"):
        if current_sequence:
            seq_string.append(current_sequence)
            current_sequence = ""
        seq_name.append(line[1:]) 
    else:
        current_sequence += line.strip()
if current_sequence:
    seq_string.append(current_sequence)  

seq_len = len(seq_string)  
str_len = len(seq_string[0])  

symbol = ["A", "C", "G", "T"]
consensus_string = ""
profile_matrix = np.zeros(shape=(4, str_len), dtype=int)

for c in range(str_len):
    position_symbol = [s[c] for s in seq_string]
    most_common_symbol = max(position_symbol, key=position_symbol.count)
    consensus_string += most_common_symbol
    for r in range(len(symbol)):
        profile_matrix[r][c] = position_symbol.count(symbol[r])

print(consensus_string)

for i in range(len(symbol)):
    print("{}: {}".format(symbol[i], " ".join(map(str, profile_matrix[i]))))
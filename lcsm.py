def shortest_seq(seq):
    min_len = 10000
    shortest_seq = ''
    for i in seq.keys():
        if len(seq[i]) < min_len:
            min_len = len(seq[i])
            shortest_seq = seq[i]
    return shortest_seq

def shared_motif(seq):
    s_seq = shortest_seq(seq)
    motif = set()
    for i in range(len(s_seq)):
        for j in range(i + 1, len(s_seq) + 1):
            motif.add(s_seq[i:j])
    for s in seq.values():
        motif_copy = set(motif)  
        for m in motif_copy:
            if m not in s:
                motif.remove(m)  
    n = 0
    longest_motif = ''
    for i in motif:
        if len(i) > n:
            longest_motif = i
            n = len(i)
    return longest_motif

fasta_data = '''>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA'''

seq = {}
current_label = ""
for line in fasta_data.splitlines():
    if line.startswith(">"):
        current_label = line[1:]
        seq[current_label] = ""
    else:
        seq[current_label] += line.strip()

result = shared_motif(seq)
print(result)

# i have done this work on google colab and this program always works there
# but when i execute it in vsc it gives me the wrong output on the first try
# and it works the second time
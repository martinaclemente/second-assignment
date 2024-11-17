def reverse_complement(seq):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join(complement[base] for base in reversed(seq))

def find_reverse_palindromes(dna):
    dna = dna.replace('\n', '').replace(' ', '')  

    results = []
    n = len(dna)

    for length in range(4, 13):
        for start in range(n - length + 1):
            substring = dna[start:start + length]
            if substring == reverse_complement(substring):
                results.append((start + 1, length))

    results.sort()  

    return results

dna = '''TCAATGCATGCGGGTCTATATGCAT'''

reverse_palindromes = find_reverse_palindromes(dna)

for position, length in reverse_palindromes:
    print(position, length)
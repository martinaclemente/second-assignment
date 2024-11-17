from math import comb

def mendelian_inheritance(k, N):
    n = 2**k
    p = 0.25 
    prob_less_than_N = sum(comb(n, m) * (p**m) * ((1-p)**(n-m)) for m in range(N))
    prob_at_least_N = 1 - prob_less_than_N
    return prob_at_least_N
k = 2
N = 1
print(f"{mendelian_inheritance(k, N):.3f}")
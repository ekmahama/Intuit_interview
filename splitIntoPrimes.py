def dp(s):
    C = [0]*(len(s)+1)
    for i in range(1, len(s)+1):
        C[i] = sum(C[j] for j in range(i) if isprime[int(s[j:i])])
        C[i] += isprime[int(s[:i])]
    return C[len(s)]


print(dp('3175'))

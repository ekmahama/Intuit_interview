def partionString(S, X):
    ret = []
    for i in range(0, len(S), X):
        tmp = S[i:X+i]
        ret.append(sorted(list(set(tmp))))
    return ret


def findValid(S, X, N, K):
    parts = partionString(S, X)
    weight = 1
    r_weights = []
    for part in reversed(parts):
        r_weights.append(weight)
        weight *= len(part)

    ans = []
    K -= 1
    i = 0
    for weight in reversed(r_weights):
        n, K = divmod(K, weight)
        ans.append(parts[i][n])
        i += 1

    return int(''.join(ans))


S = '123456789'
X = 3
K = 4
N = len(S)
findValid(S, X, N, K)

"""You have an array Arr of N numbers ranging from 0 to 99. Also you have Q queries [L, R]. For each such query you must print
V([L, R]) = ∑i=0..99 count(i)2 * i where count(i) is the number of times i occurs in Arr[L..R].

Steps:
- Let BLK_SIZE = int(sqrt(N))
- Rearrange all queries in what we call Mo's order: this is done as follows:[L1,R1] comes before [L2,R2] iff:
    1) L1/BLK_SIZE < L2/BLK_SIZE
    2)L1/BLK_SIZE== L2/NLK_SIZE && R1 < R2
- Maintain  a segment [mo_left, mo_right] for which we know Func([mo_left, mo_right]). Initially the segment is empy.=> mo_left=0
    mo_right =-1

- Answer all queries following Mo’s order. Suppose the next query you want to answer is [L, R]. Then you perform these steps:
   while mo_right is less than R, extend current segment to [mo_left, mo_right + 1];
   b) while mo_right is greater than R, cut current segment to [mo_left, mo_right - 1];
   c) while mo_left is greater than L, extend current segment to [mo_left - 1, mo_right];
   d) while mo_left is less than L, cut current segment to [mo_left + 1, mo_right].
This will take O( (|left - L| + |right - R|) * F) time, because we required that each extension\deletion is performed in O(F) steps.
After all transitions, you will have mo_left = L and mo_right = R, which means that you have successfully computed Func([L, R]).

"""

from math import sqrt


from collections import defaultdict


def answerQueries(arr, Q):

    def add(i, current_answer, cnt):
        current_answer -= cnt[i]*cnt[i]*i
        cnt[i] += 1
        current_answer += cnt[i]*cnt[i]*i
        return current_answer

    def remove(i, current_answer, cnt):
        current_answer -= cnt[i]*cnt[i]*i
        cnt[i] -= 1
        current_answer += cnt[i]*cnt[i]*i
        return current_answer

    def evenFreqChek(freqCnt):
        ret = True
        for i in range(len(freqCnt)):
            if freqCnt[i] % 2:
                ret = False
                break
            # print(f'{freqCnt[i]}')
        return ret

    N = len(arr)
    BLK_SIZE = int(sqrt(N))
    freqCnt = [0, ]*N
    current_answer = 0

    Q_rest = defaultdict(list)

    # Sort Queries
    mo_order = sorted(Q, key=lambda x: (int(x[0]/BLK_SIZE), x[1]))

    # Setting up mo segment
    mo_left, mo_right = 0, -1
    for L, R in mo_order:
        while True:
            if mo_right < R:
                mo_right += 1
                current_answer = add(arr[mo_right], current_answer, freqCnt)

            elif mo_right > R:
                current_answer = remove(arr[mo_right], current_answer, freqCnt)
                mo_right -= 1

            elif mo_left < L:
                current_answer = remove(arr[mo_left], current_answer, freqCnt)
                mo_left += 1

            elif mo_left > L:
                mo_left -= 1
                current_answer = add(arr[mo_left], current_answer, freqCnt)
            elif mo_left == L and mo_right == R:
                break

        Q_rest[(L, R)].append(
            (current_answer, evenFreqChek(freqCnt)))
    return Q_rest


arr = [0, 1, 1, 1, 2, 2, 4, 1, 3, 5, 1, 5, 3, 5, 4, 0, 2, 2]
Q = [[0, 8], [2, 5], [2, 11], [16, 17], [13, 14], [1, 17], [17, 17]]


res = answerQueries(arr, Q)
print()

from collections import defaultdict


class Solution:
    def findError(self, input):
        res = defaultdict(set)

        for action, user in input:
            res[user].add(action)

        ret = []
        for k, val in res.items():
            if ''.join(sorted(val)) == 'ABC':
                ret.append(k)
        return ret


input = [
    ["A", "1"],
    ["A", "1"],
    ["A", "1"],
    ["B", "1"],
    ["B", "2"],
    ["C", "2"],
    ["C", "2"],
    ["C", "3"],
    ["A", "2"],
    ["A", "3"],
    ["A", "2"],
    ["B", "2"],
    ["C", "2"],
]

Solution().findError(input)

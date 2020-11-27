def substrCalc(s):
    res = []

    def helper(s):
        if not s:
            return
        if s not in res:
            res.append(s)
        helper(s[1:])
        helper(s[:-1])

        if len(s) >= 2:
            helper(s[1:-1])

    helper(s)
    return res


s = 'abcde'
ret = substrCalc(s)
print(ret)

from collections import defaultdict


def subdomainVisits(cpdomains):
    res = defaultdict(int)

    for d in cpdomains:
        cnt, domains = d.split()
        cnt = int(cnt)

        frags = domains.split('.')
        for i in range(len(frags)):
            res['.'.join(frags[i:])] += cnt

    return [f'{c} {d}' for d, c in res.items()]

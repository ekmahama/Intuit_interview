from collections import defaultdict


def subdomainVisits(cpdomains):
    output = defaultdict(int)
    for d in cpdomains:
        cnt, domains = d.split()
        frags = domains.split('.')

        for i in range(len(frags)):
            output['.'.join(frags[i:])] += int(cnt)
    return [f'{c} {d}' for d, c in output.items()]

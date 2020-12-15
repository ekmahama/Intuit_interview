from collections import defaultdict


def badRecord(input):
    if not input:
        return []

    forgot_enter = set()
    forgot_exit = set()
    logRecords = defaultdict(list)

    for name, action in input:
        if action == 'enter':
            if logRecords[name] and logRecords[name][-1] == 'enter':
                forgot_exit.add(name)
            # logRecords[name].append(action)
        else:
            if logRecords[name] and logRecords[name][-1] == 'exit':
                forgot_enter.add(name)
        logRecords[name].append(action)
    return [list(forgot_exit), list(forgot_enter)]


input = [
    ["Paul",  "enter"],
    ["Paul",  "enter"],
    ["Curtis", "enter"],
    ["Paul", "exit"],
    ["John", "exit"],
    ["Paul", "exit"],
    ["Jennifer", "exit"],
    ["Curtis", "exit"],
    ["John", "enter"],
    ["Jennifer", "enter"],
    ["Curtis",  "enter"],
    ["John", "enter"],
    ["Jennifer", "enter"],
    ["John", "exit"],
    ["Curtis", "exit"],
    ["Jennifer", "exit"],
]

res = badRecord(input)
print()

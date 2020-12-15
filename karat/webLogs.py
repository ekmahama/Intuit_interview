from collections import defaultdict


def findMinMax(logs):
    output = defaultdict(list)
    result = defaultdict(list)

    for time, user, _ in logs:
        output[user].append(time)

    for user, times in output.items():
        result[user].append(min(times))
        result[user].append(max(times))
    return result


logs = [
    ["58523", "user_1", "resource_1"],
    ["62314", "user_2", "resource_2"],
    ["54001", "user_1", "resource_3"],
    ["200", "user_6", "resource_5"],
    ["215", "user_6", "resource_4"],
    ["54060", "user_2", "resource_3"],
    ["53760", "user_3", "resource_3"],
    ["58522", "user_4", "resource_1"],
    ["53651", "user_5", "resource_3"],
    ["2", "user_6", "resource_1"],
    ["100", "user_6", "resource_6"],
    ["400", "user_7", "resource_2"],
    ["100", "user_8", "resource_2"],
    ["54359", "user_1", "resource_3"],
]

res = findMinMax(logs)
print()

from collections import defaultdict


def find_pairs(pairs):
    if not pairs or not pairs[0]:
        return []
    result = defaultdict(list)
    d = defaultdict(list)

    for student, course in pairs:
        d[student].append(course)

    student_id = list(d.keys())

    for i in range(len(student_id)-1):
        for j in range(i+1, len(student_id)):
            common = findCommon(d, student_id[i], student_id[j])
            if not common:
                result[(student_id[i], student_id[j])]
                continue
            for course in common:
                result[(student_id[i], student_id[j])].append(course)
    return result


def findCommon(d, i, j):
    return list(set(d[i]) & set(d[j]))


pairs = [
    ["58", "Linear Algebra"],
    ["94", "Art History"],
    ["94", "Operating Systems"],
    ["17", "Software Design"],
    ["58", "Mechanics"],
    ["58", "Economics"],
    ["17", "Linear Algebra"],
    ["17", "Political Science"],
    ["94", "Economics"],
    ["25", "Economics"],
    ["58", "Software Design"],
]
res = find_pairs(pairs)

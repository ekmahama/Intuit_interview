from collections import defaultdict, deque


def canFinish(numCourse, prerequisites):
    adjaList = defaultdict(list)
    ranks = [0, ]*numCourse

    # the dict keys are the prerequisite for the course
    # For ranks array: index represent the courses and the values represent the
    # the rank or number of dependencies
    for course, prereq in prerequisites:
        adjaList[prereq].append(course)
        ranks[course] += 1

    queue = deque()
    # add not with no dependency to rank 0
    for course, rank in enumerate(ranks):
        # If a course has not dependency i.e. rank ==0, take it first
        if rank == 0:
            queue.append(course)
            print(f'First : {course}')

    # Topological sorting
    #BFS or Khan
    visited = set()
    while queue:
        course = queue.popleft()
        visited.add(course)
        numCourse -= 1

        # reduce neighbor rank by 1
        # add not with no dependency to rank 0
        for neigh in adjaList[course]:
            ranks[neigh] -= 1
            if ranks[neigh] == 0 and neigh not in visited:
                queue.append(neigh)

    print(f'Last : {course}')
    return not numCourse


if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[1, 0], [0, 2], [1, 2], [2, 3]]
    canFinish(numCourses, prerequisites)

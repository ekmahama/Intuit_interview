from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adjaList = defaultdict(list)
        ranks = [0, ]*numCourses

        for course, prereq in prerequisites:
            adjaList[prereq].append(course)
            ranks[course] += 1

        q = deque()
        for course, rank in enumerate(ranks):
            if rank == 0:
                q.append(course)

        visited = set()
        while q:
            c = q.popleft()
            visited.add(c)
            res.append(c)
            numCourses -= 1

            for neigh in adjaList[c]:
                ranks[neigh] -= 1
                if ranks[neigh] == 0 and neigh not in visited:
                    q.append(neigh)

        return res if not numCourses else []

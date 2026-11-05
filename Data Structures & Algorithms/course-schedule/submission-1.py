from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        adj = [[] for _ in range(numCourses)]   # prereq -> courses it unlocks
        indegree = [0] * numCourses             # how many prereqs each course still needs

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        # Start with courses that need nothing
        queue = deque(c for c in range(numCourses) if indegree[c] == 0)
        done = 0

        while queue:
            c = queue.popleft()
            done += 1                    # take this course
            for nxt in adj[c]:           # it unlocks these courses
                indegree[nxt] -= 1       # one fewer prerequisite outstanding
                if indegree[nxt] == 0:   # all prerequisites met
                    queue.append(nxt)

        return done == numCourses        # stuck courses mean a cycle
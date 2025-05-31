class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import deque

        # 1) Build graph + in-degree
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        # 2) Seed queue with all courses having in-degree 0
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []

        # 3) Kahn’s topological sort
        while q:
            u = q.popleft()
            order.append(u)
            for nxt in adj[u]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        # 4) If we scheduled all courses, return the order; otherwise return []
        return order if len(order) == numCourses else []

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # distances = {}
        # for x,y in points:
        #     key = x**2 + y**2
        #     if key not in distances: distances[key]=[]
        #     distances[key].append([x,y])
        # sorted_points = [point for key, value in sorted(distances.items()) for point in value]
        # return sorted_points[:k]

        # return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:k]

        heap = [(x*x + y*y, [x,y]) for x,y in points]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]

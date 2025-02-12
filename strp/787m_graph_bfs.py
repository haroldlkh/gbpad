class Solution:
  def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    space = defaultdict(list)
    visited = [float('inf')]*n
    visited[src] = 0

    for flight in flights:
        space[flight[0]].append((flight[1],flight[2]))

    queue = deque([(src,0)])
    k+=1

    while k>0 and queue:
        size = len(queue)
        while size>0:
            curr_node, curr_price = queue.popleft()
            for neighbour, price in space[curr_node]:
                new_price = curr_price + price
                if new_price < visited[neighbour]: 
                    visited[neighbour] = new_price
                    queue.append((neighbour, new_price))
            size-=1
        k-=1
    # return visited
    return visited[dst] if visited[dst] != float('inf') else -1


# Time complexity: O(Node + Flights)
# Space complexity: O(Node + Flights)
# Total Space Complexity
# Since the adjacency list space takes O(E) and the other data structures (visited and queue) take O(N), the total space complexity is: O(N + E)
#
# This accounts for:
# O(N) for the visited array (storing the minimum cost to each node).
# O(E) for the adjacency list representation (storing all edges).
# O(N) for the queue (if all nodes are processed).
# Thus, the final worst-case space complexity is: O(N + E)

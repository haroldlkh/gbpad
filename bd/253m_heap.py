class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq

        ongoing  = []
        needed_rooms = 0

        for start, end in sorted(intervals, key=lambda x: x[0]):
            # if len(ongoing)>0 and ongoing[0] <= start:
            #     heapq.heappop(ongoing)
            # if needed_rooms == len(ongoing):
            #     needed_rooms +=1
            # heapq.heappush(ongoing, end)
            if len(ongoing)>0 and ongoing[0] <= start:
                heapq.heapreplace(ongoing,end)
            else: heapq.heappush(ongoing, end)
        return len(ongoing) #needed_rooms

'''
start: [[1,5],[8,9],[8,9]]
already sorted
p1:
    ongoing = []
    need = 0
    len(ongoing) = 0 > 0 False: no need to pop

    needed = ongoing
        needed = 1
        ongoing = [5]

p2:
    len(ongoing) = 1 > 0 and 5 <= 8 True:
        pop: ongoing 


'''
'''
order meetings by which starts first

initially
    needed rooms = 0
    used rooms = 0
i have a meeting, I need to give it a room
    if available rooms = 0, used and needed rooms + 1

make room available when a meeting ends

have another meeting
    check if room is available
'''

'''
[[0,30],[5,10],[15,20]]
needed rooms = 0
used rooms = 0
earliest meeting ends = 0

p1:
    [0,30]
    available rooms = needed - used = 0 - 0 = 0
        needed rooms = 1
        used rooms = 1
        ends at 30

p2:
    [5, 10]
    start of this meeting < end of ongoing meeting
        needed rooms + 1 = 2
        available rooms = needed - used = 1
        used rooms + 1 = 2
        end at 30 (what about 10?)
            longest = 30
            earliest = 10

p3:
    [15,20]
    start of this meeting > end of earliest meeting:
        used rooms - 1 = 1
        available rooms = needed - used = 2 - 1 = 1
        Used rooms = 2
        earliest end = 20

I need to collection when meeting ends, and store it least to largest. min heap

'''

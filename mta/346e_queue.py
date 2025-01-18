class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.runningsum = 0
        self.length = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.runningsum += val
        self.length +=1
        # if len(self.queue)>self.size:  
        if self.length > self.size:
            self.length-=1          
            self.runningsum -= self.queue.popleft()
        # return self.runningsum/len(self.queue)
        return self.runningsum/self.length


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

class NestedListIterator:
    def __init__(self, lst):
        self.stack = [[0, lst]]
    def hasNext(self):
        while len(self.stack)>0:
            i, lst = self.stack[-1]
            if i >= len(lst):
                self.stack.pop()
            elif isinstance(lst[i], list):
                self.stack[-1][0] += 1
                self.stack.append([0, lst[i]])
            else: return True
        return False
    def next(self):
        i, lst = self.stack[-1]
        self.stack[-1][0] += 1
        return lst[i]

# iterator = NestedListIterator([1,[[2,3],4],5])
tests = [
         NestedListIterator([1,2,3])
        #  NestedListIterator([1,[[2,3],4],5]),
        #  NestedListIterator([1,[],5]),
        #  NestedListIterator([1,[]]),
        #  NestedListIterator([1,[[]],5]),
        #  NestedListIterator([1,[[]]]),
        ]

for test in tests:
    res = []
    while test.hasNext():
        res.append(test.next())
    print(res)

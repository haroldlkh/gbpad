def overlap(arr1,arr2):
    p1,p2=0,0
    n1,n2=len(arr1),len(arr2)
    res = []
    while p1<n1 and p2<n2:
        int1,int2 = arr1[p1], arr2[p2]
        if int1[1]<int2[0]: p1+=1
        elif int2[1]<int1[0]: p2+=1
        else:
            start = max(int1[0],int2[0])
            end = min(int1[1],int2[1])
            res.append([start,end])
            if int1[1]<int2[1]: p1+=1
            else: p2+=1

    return res

tests = [([[0, 1], [4, 6], [7, 8]], [[2, 3], [5, 9], [10, 11]], [[5, 6], [7, 8]]),
         ([[2, 4], [5, 8]], [[3, 3], [4, 7]], [[3, 3], [4, 4], [5, 7]]),
         ([],[1,2],[])]

for arr1,arr2, expected in tests:
    got = overlap(arr1,arr2)
    assert got == expected, f"{arr1}, {arr2}. got {got}, expected {expected}"

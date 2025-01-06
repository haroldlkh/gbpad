class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i,j = 0,0
        intersection = []
        while i<len(firstList) and j<len(secondList):
            # if firstList[i][0] > secondList[j][1]: j+=1
            # elif firstList[i][1] < secondList[j][0]: i+=1

            # # B ahead of A
            # elif firstList[i][1] >= secondList[j][0] and firstList[i][1] < secondList[j][1] and firstList[i][0] < secondList[j][0]:
            #     intersection.append([secondList[j][0],firstList[i][1]])
            #     i+=1
            # # B behind A
            # elif firstList[i][0] <= secondList[j][1] and firstList[i][1] > secondList[j][1] and firstList[i][0] > secondList[j][0]:
            #     intersection.append([firstList[i][0],secondList[j][1]])
            #     j+=1
            # # A in B or B in A
            # elif firstList[i][0] >= secondList[j][0] and firstList[i][1] <= secondList[j][1]:
            #     intersection.append([firstList[i][0],firstList[i][1]])
            #     i+=1
            # elif firstList[i][0] <= secondList[j][0] and firstList[i][1] >= secondList[j][1]:
            #     intersection.append([secondList[j][0],secondList[j][1]])
            #     j+=1

            left = max(firstList[i][0],secondList[j][0])
            right = min(firstList[i][1],secondList[j][1])

            if left <= right: intersection.append([left,right])

            if firstList[i][1] > secondList[j][1]: j+=1
            else: i+=1
            
        return intersection

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        import heapq
        # Build a max-heap of (–count, char), skipping zero counts
        heap = [(-cnt, ch) for ch, cnt in (('a',a),('b',b),('c',c)) if cnt]
        heapq.heapify(heap)

        result = []

        while heap:
            cnt1, ch1 = heapq.heappop(heap)

            if len(result)>=2 and result[-1]==ch1 and result[-2]==ch1:
                if not heap: break
                cnt2, ch2 = heapq.heappop(heap)
                result.append(ch2)
                cnt2+=1
                if cnt2<0: heapq.heappush(heap, (cnt2, ch2))
                heapq.heappush(heap,(cnt1, ch1))
            else:
                result.append(ch1)
                cnt1+=1
                if cnt1<0: heapq.heappush(heap,(cnt1,ch1))

        return ''.join(result)

    # t=n log k, where k is number of unique chars (3 in this case)
    # space=n where n is sum of unique chars
    # heapq is implemented as smallest on top, so inverse is largest.

      
    # def longestDiverseString(self, a: int, b: int, c: int) -> str:
    #     choices = {'a': a, 'b': b, 'c':c}
    #     def clean(d):
    #         return {k:v for k,v in d.items() if v>0}
    #     choices = clean(choices)
    #     if len(choices)==0: return ''

    #     s=[]

    #     pick = max(choices,key=choices.get)
    #     last_pick=pick
    #     choices[pick]-=1
    #     choices=clean(choices)
    #     s.append(pick)
    #     valid_choices = choices
        
    #     while len(valid_choices)>0:
    #         pick = max(valid_choices,key=valid_choices.get)
    #         choices[pick]-=1
    #         s.append(pick)
    #         choices = clean(choices)
    #         if last_pick == pick: valid_choices = {k:v for k,v in choices.items() if k!=pick}
    #         else: valid_choices = choices
    #         last_pick=pick

    #     return ''.join(s)

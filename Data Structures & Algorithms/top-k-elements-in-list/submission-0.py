class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()

        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i] = 1

        print(count)

        rank = [[] for i in range(len(nums))]        
        print(rank)

        for key in count:
            rank[count[key]-1].append(key)

        print(rank)
        output = []

        for x in reversed(rank):
            for i in x:
                output.append(i)
                k-=1
            if(k == 0):
                break

        return output

            


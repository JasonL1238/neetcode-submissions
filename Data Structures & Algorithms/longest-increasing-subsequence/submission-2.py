class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        m = dict()
        for i in nums:
            keys = list(m.keys())
            needAdd = True
            for k in keys:
                if i > k:
                    if i in m:
                        m[i] = max(m[k]+1,m[i])
                    else:
                        m[i] = m[k]+1
                    needAdd = False
            if needAdd:
                m[i] = 1
        
        values = m.values()
        output = 1
        for i in values:
            output = max(i,output)
        print(m)

        return output
            
            
                
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        for i in range(len(gas)):
            total += gas[i]
            total -= cost[i]
        
        if total < 0:
            return -1
        
        curr = 0
        output = 0 
        i = 0
        while i < len(gas):
            curr += gas[i]
            curr -= cost[i]
            if curr < 0:
                curr = 0
                output = i + 1
            i += 1
        

        return output



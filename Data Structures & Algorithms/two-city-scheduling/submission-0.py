class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        temp = []

        for k in range(len(costs)):
            i = costs[k]
            a = i[0]
            b = i[1]
            diff = a-b
            temp.append((diff,k))
        
        temp.sort()

        output = 0

        n = int(len(costs)/2)

        for i in range(n):
            index = temp[i][1]
            output += costs[index][0]

        for i in range(n,2*n):
            index = temp[i][1]
            output += costs[index][1]
        
        return output
        

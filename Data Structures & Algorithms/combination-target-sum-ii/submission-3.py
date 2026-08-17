class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        output = dict()
        curr = []
        s = 0

        def dfs(i):
            nonlocal s

            if s == target and not tuple(curr) in output:
                output[tuple(curr)] = curr.copy()
                
            
            if s < target and i < len(candidates):



                curr.append(candidates[i])
                s += candidates[i]
                dfs(i+1)

                nextIndex = i+1
                while nextIndex < len(candidates) and candidates[nextIndex] == candidates[i]:
                    nextIndex+=1
                    
                curr.pop()
                s -= candidates[i]
                dfs(nextIndex)


        
        dfs(0)

        return list(output.values())


            

        
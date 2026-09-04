class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        output = [0,0,0]
        
        for triplet in triplets:
            a = triplet[0]
            b = triplet[1]
            c = triplet[2]
            
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            else:
                if a == target[0] and not output[0] == target[0]:
                    output[0] = max(a,output[0])
                    output[1] = max(b,output[1])
                    output[2] = max(c,output[2])
                elif b == target[1] and not output[1] == target[1]:
                    output[0] = max(a,output[0])
                    output[1] = max(b,output[1])
                    output[2] = max(c,output[2])
                elif c == target[2] and not output[2] == target[2]:
                    output[0] = max(a,output[0])
                    output[1] = max(b,output[1])
                    output[2] = max(c,output[2])

                
        return output == target


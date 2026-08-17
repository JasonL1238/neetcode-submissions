class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        indices = [len(strs)]

        table = dict()

        for i in range(len(strs)):
            key = [0] * 26
            for char in strs[i]:
                index = ord(char.lower()) - 97
                key[index]+=1
            keyStr = tuple(key)
            if keyStr in table:
                table[keyStr].append(strs[i])
            else:
                table[keyStr] = [strs[i]]
        
        return list(table.values())

        


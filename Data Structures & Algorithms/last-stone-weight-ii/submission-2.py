class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2

        pos = {0}

        for stone in stones:
            for weight in list(pos):
                new = weight + stone
                if new <= target:
                    pos.add(new)
        
        a = max(list(pos))
        b = total - a
        return b - a





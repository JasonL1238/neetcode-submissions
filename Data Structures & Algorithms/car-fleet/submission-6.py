class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int: 

        tupleArr = []

        for i in range(len(position)):
            obj = (position[i],speed[i])
            tupleArr.append(obj)

        tupleArr.sort(key=lambda x: x[0])

        times = []
        for i in range(len(tupleArr)):
            times.append((target-tupleArr[i][0])/tupleArr[i][1])
        

        print(times)
        print(tupleArr)
        final = []

        while len(times) > 1:
            first = times.pop()
            second = times.pop()
            if first < second:
                final.append(first)
                times.append(second)
            else:
                times.append(first)
                
        print(final)
        return len(final) + 1
            


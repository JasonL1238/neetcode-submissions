class TimeMap:

    def __init__(self):
        self.m = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.m:
            self.m[key].append((timestamp,value))
        else:
            self.m[key] = [(timestamp,value)]
            

    def get(self, key: str, timestamp: int) -> str:
        print(key)
        print(self.m)
        if key in self.m:
            arr = self.m[key]
            l = 0
            r = len(arr) - 1
            closest = float("-inf")
            while l <= r:
                m = (l+r)//2
                if arr[m][0] < timestamp:
                    closest = max(m,closest)
                if arr[m][0] == timestamp:
                    return arr[m][1]
                elif arr[m][0] > timestamp:
                    r = m -1
                else:
                    l = m + 1
            if closest == float("-inf"):
                return ""
            return arr[closest][1]
        else:
            return ""

        

        

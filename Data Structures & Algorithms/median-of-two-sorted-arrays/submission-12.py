class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        half = (m+n)//2

        A = nums1
        B = nums2



        if n > m:
            A = nums2
            B = nums1

        l = 0
        r = len(A)
        i = (r+l)//2
        j = half-i

        AL = A[i-1] if i >= 1 else float("-infinity")
        AR = A[i] if i < len(A)  else float("infinity")
        BL = B[j-1] if j >= 1 else float("-infinity")
        BR = B[j] if j < len(B) else float("infinity")
        while l <= r:
            i = (r+l)//2
            j = half-i
            print("i" + str(i))
            print("j" + str(j))
            AL = A[i-1] if i >= 1 else float("-infinity")
            AR = A[i] if i < len(A) else float("infinity")
            BL = B[j-1] if j >= 1 else float("-infinity")
            BR = B[j] if j < len(B) else float("infinity")
            print("AR" + str(AR))
            print("AL" + str(AL))
            print("BR" + str(BR))
            print("BL" + str(BL))

            if AR >= BL and AL <= BR:
                break
            elif AR < BL:
                l = i + 1
            else:
                r = i - 1
        
        if (n+m)%2 == 0:
            return (min(AR,BR) + max(AL,BL))/2
        else:
            return min(AR,BR)
                
        



        
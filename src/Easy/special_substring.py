class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:

        # For this problem my initial asumptions are:
        # 1. Only one pass trough the array is necessary
        # 2. I must keep track of the "current character", the previous and the count.
        # 3. If count == k, return True. Else, return false.

        prev = ""
        i = 0
        count = 1 

        for i in range(len(s)):
    
            if count == k:
                if s[i-1] != s[i]:
                    return True

            if s[i] == prev:
                count += 1

            else:
                prev = s[i]
                count = 1

        return count == k
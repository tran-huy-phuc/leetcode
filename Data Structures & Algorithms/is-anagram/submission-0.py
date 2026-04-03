class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)): # O(7n) = O(n)
            sI = s[i]
            # Increase the frequency of sI
            countS[sI] = countS.get(sI, 0) + 1

            tI = t[i]
            # Increase the frequency of tI
            countT[tI] = countT.get(tI, 0) + 1

        return countS == countT # O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedS1 = sorted(s)
        sortedS2 = sorted(t)

        if (sortedS1 == sortedS2):
            return True
        else:
            return False
        
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # guard phase
        if x < 0:
            return False

        s1 = str(x)

        l = 0
        r = len(s1) - 1

        while l < r:
            if s1[l] != s1[r]:
                return False
            l = l + 1
            r = r - 1

        return True

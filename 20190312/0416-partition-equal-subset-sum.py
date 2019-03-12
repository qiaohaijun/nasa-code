class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum = 0
        for n in nums:
            sum += n

        if sum % 2 == 1:
            return False

        target_num = sum // 2

        # 01 背包问题
        dp = [False] * (target_num + 1)

        dp[0] = True

        for i in range(len(nums)):
            for j in range(target_num, -1, -1):
                if j>=nums[i]:
                    dp[j] = dp[j-nums[i]] or dp[j]

        return dp[-1]
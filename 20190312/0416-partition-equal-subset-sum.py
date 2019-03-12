class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum = 0
        for n in nums:
            sum += n

        # guard phase
        # 提前判断是否有必要继续下去
        if sum % 2 == 1:
            return False

        target_num = sum // 2

        # 01 背包问题
        dp = [False] * (target_num + 1)
        # 初始化解释
        # 针对二维情况,
        # dp[i][0] 表示的是使用前i个数字是否可以组成一个{}空集
        # 答案是肯定的
        dp[0] = True

        for i in range(len(nums)):
            for j in range(target_num, -1, -1):
                # 等号的含义, 如果不取等号, 那么就是说j不能取nums[i]中的任意一个.
                # 而实际是我们要取该数
                if j>=nums[i]:
                    dp[j] = dp[j-nums[i]] or dp[j]

        return dp[-1]
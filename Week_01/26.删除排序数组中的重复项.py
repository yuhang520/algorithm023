# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 审题：
        #     1、是排序数组
        #     2、不需要考虑长度的问题
        # 边界情况：
        #
        # 可用解法：
        #     1、暴力循环去重
        #     2、双指针
        p = 0
        q = 1
        while q < len(nums):
            if nums[p] == nums[q]:
                q += 1
            else:
                nums[p + 1] = nums[q]
                p += 1
                q += 1
        return len(nums[:p + 1])

# leetcode submit region end(Prohibit modification and deletion)





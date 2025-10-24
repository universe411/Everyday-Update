class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # 先排序

        for i, a in enumerate(nums):  # 外层循环 枚举三元组的第一个数
            if a > 0:  # pruning 如果a>0 其后的数都会>0 三数之和不可能为0
                break

            if i > 0 and a == nums[i - 1]:  # 去重 如果当前a和前一个一样 跳过
                continue

            # 设定左右指针：在 a 右侧区间 [i+1, …, n-1] 搜索另外两个数
            l, r = i + 1, len(nums) - 1
            while l < r:  # 只要左右未交错，就持续尝试
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:  # 和太大：右指针左移，尝试更小的数以减小总和
                    r -= 1
                elif three_sum < 0:  # 和太小：左指针右移，尝试更大的数以增大总和
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1  # 命中后同时收缩两端
                    while nums[l] == nums[l - 1] and l < r:
                        # 去重（针对左指针）：跳过与刚用过的左值相同的连续元素，避免重复三元组
                        l += 1
        return res

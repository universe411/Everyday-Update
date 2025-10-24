"""
Given an array of integers nums, return the length of the longest consecutive sequence 
of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 
1 greater than the previous element. 
The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.
    """


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert list to set
        # set: duplicates are removed
        numSet = set(nums)
        # initilize the answer
        longest = 0

        # iterate over each distinct number over set
        for num in numSet:
            # 只从序列开头开始数
            # 如果num-1不在set里，说明num前面没有紧邻的数，是起点
            if (num - 1) not in numSet:
                length = 1  # 初始长度为1（至少包含num自己）
                while (num + length) in numSet:
                    length += 1  # 从起点num开始往右尝试num+1，+2，是否存在
                    # 存在的话，长度就+1

                longest = max(length, longest)  # update maximum with the
                # length  of this sequence if longer
        return longest

#!/usr/bin/env python
# coding=utf-8

"""
题目：
    在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
解法：
    1) 先排序再取第k大的元素， 时间复杂度O(nlogn)
    2) 大顶堆：建立大小为K的大顶堆，时间复杂度为O(nlogK)
    3) 快速选择
       寻找第K大的数，即N - K小的数，使用快速排序
       eg.  [5,5,2,1,4] N = 5, K=2，找到N-K=3（下标为3）pivot
"""
import random
class Solution:
    def findKthLargest(self, nums, k):
        length = len(nums)
        return self.kthLargest(nums, 0, length - 1, length - k)

    def kthLargest(self, nums, left, right, k):
        """

        :param nums:
        :param left:
        :param right:
        :param k:
        :return:
        """
        if left == right:
            return nums[left]

        pivot = self.partition(nums, left, right)
        if pivot == k:
            return nums[pivot]
        elif pivot < k:
            return self.kthLargest(nums, pivot + 1, right, k)
        return self.kthLargest(nums, left, pivot - 1, k)

    def partition(self, nums, left, right):
        """
        随机选择一个元素按大小切分数组
        :param nums:
        :param left:
        :param right:
        :return:
        """

        # 随机选择一个作为pivot，然后与left交换，后面按照正统的快速选择处理代码：pivot为left第一个
        pivot = random.randrange(left, right + 1)
        nums[left], nums[pivot] = nums[pivot], nums[left]

        low, high = left, right
        temp = nums[low]

        while low < high:
            # 从右开始遍历，找到第一个小于等于pivot的数，然后替换到左边大于等于pivot的数，左边第一个为pivot默认可以替换
            while low < high and nums[high] > temp:
                high -= 1
            nums[low] = nums[high]

            # 从左往右遍历，找到第一个大于pivot的数，然后替换到右边小于的数
            while low < high and nums[low] <= temp:
                low += 1
            nums[high] = nums[low]

        # 替换pivot到对应位置
        nums[high] = temp

        return high

nums = [5,5,2,1,6,8,3,7,9]
solution = Solution()
print(solution.findKthLargest(nums, 6))
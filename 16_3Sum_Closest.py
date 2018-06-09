"""
No.16  3Sum Closest

Description

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution:
	def threeSumClosest(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		nums.sort()
		res = nums[0] + nums[1] + nums[2]
		for i in range(len(nums) - 2):
			left = i + 1
			right = len(nums) - 1
			while left < right:
				if nums[left] + nums[right] < target - nums[i]:
					if abs(nums[left] + nums[right] + nums[i] - target) < abs(res - target):
						res = nums[left] + nums[right] + nums[i]
					"""
					while left + 1 < right and nums[left] == nums[left + 1]:
						left += 1
					"""
					left += 1
				elif nums[left] + nums[right] > target - nums[i]:
					if abs(nums[left] + nums[right] + nums[i] - target) < abs(res - target):
						res = nums[left] + nums[right] + nums[i]
					right -= 1
				else:
					return target
		return res
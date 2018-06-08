'''
15.3Sum
Description:
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution:
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		nums.sort()
		res = []
		for i in range(len(nums)):
			if res != [] and nums[i] == res[-1][0]:
				continue
			left = i + 1
			right = len(nums) + 1
			while right > left:
				if nums[left] + nums[right] > -nums[i]:
					right -= 1
				elif nums[left] + nums[right] < -nums[i]:
					left += 1
				else:
					if res == [] or res[-1] != [nums[i], nums[left], nums[right]]:
						res.append([nums[i], nums[left], nums[right]])
					left += 1
					right -= 1
		return res
		
	def threeSum2(self, nums):
		nums.sort()
		res = []
		for i in range(len(nums) - 2):
			if nums[i] > 0:
				break
			if (i > 0 and nums[i] == nums[i-1]):
				continue
			left = i + 1
			right = len(nums) - 1
			while(left < right):
				if nums[left] + nums[right] == -nums[i]:
					res.append([nums[i], nums[left], nums[right]])
					temp = nums[left]
					while left < right and nums[left] == temp:
						left += 1
					temp = nums[right]
					while left < right and nums[right] == temp:
						right -= 1
				elif nums[left] + nums[right] < -nums[i]:
					left += 1
				else:
					right -= 1
		return res
					
					
					
					
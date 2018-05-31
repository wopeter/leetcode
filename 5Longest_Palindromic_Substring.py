"""
5. Longest Palindromic Substring
Description:
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.


Example 2:
Input: "cbbd"
Output: "bb"

"""


class Solution:
	def longestPalindrome(self, s):
		if s == s[::-1]:
			return s
		maxLen = 1
		start = 0
		for i in range(1, len(s)):
			if i - maxLen >= 0 and s[i-maxLen:i+1] == s[i-maxLen:i+1][::-1]:
				start = i - maxLen
				maxLen = maxLen + 1
			elif i - maxLen >= 1 and s[i-maxLen-1:i+1] == s[i-maxLen-1:i+1][::-1]:
				start = i - maxLen -1
				maxLen += 2
		return s[start:start+maxLen]
		
	def longestPalindrome2(self, s):
		 res = ""
        p = [[None for i in range(len(s))] for i in range(len(s))]
        for j in range(len(s)):
            for i in range(j+1):
                if i == j:
                    p[i][j] = True
                elif i+1 == j:
                    p[i][j] = (s[i] == s[j])
                else:
                    p[i][j] = (p[i+1][j-1] and (s[i] == s[j]))
        for j in range(len(s)):
            for i in range(j, -1, -1):
                if p[i][j]:
                    if len(res) < (j-i+1):
                        res = s[i:j+1]
                    #res = s[i:j+1] if len(res) < (j-i+1)
        return res
	
	def 
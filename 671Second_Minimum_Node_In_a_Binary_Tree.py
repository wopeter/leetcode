'''
671.Second Minimum Node In a Binary Tree
Description:
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input:
   2
  / \
 2   5  
    / \
   5   7
Output:5
Explanation: The smallest value is 2, the second smallest value is 5.
'''
class Solution(object):
	def findSecondMinimumValue(self, root):
		def dfs(node):
			if node:
				uniques.add(node.val)
				dfs(node.left)
				dfs(node.right
		uniques = set()
		dfs(root)
		
		min1, ans = root.val, float('inf')
		for v in uniques:
			if min1 < v < ans:
				ans = v
		return ans if ans < float('inf') else -1
		
	def findSecondMinimumValue2(self, root):
		self.ans = float('inf')
		min1 = root.val
		
		def dfs(node):
			if node:
				if min1 < node.val < self.ans:
					self.ans = node.val
				elif node.val == min1:
					dfs(node.left)
					def(node.right)
		dfs(root)
		
		return self.ans if self.ans < float('inf') else -1
	
	def findSecondMinimumValue3(self, root):
        def findMinimumValue(node, v):
            if node == None:
                return -1
            if node.val > v:
                return node.val
            if node.val == v:
                l = findMinimumValue(node.left, v)
                r = findMinimumValue(node.right, v)
                if  l == -1 and  r == -1:
                    return -1
                elif l == -1:
                    return r
                elif r == -1:
                    return l
                else:
                    return min(r, l)
        if root == None:
            return -1
        return findMinimumValue(root, root.val)
				
				
				
				
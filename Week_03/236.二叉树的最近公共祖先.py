#二叉树的最近公共祖先：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
#definition for a binary tree node
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
class Solution:
    def lowestCommonAncestor(self,root:'TreeNode',p:"TreeNode",q:"TreeNode"):
        #审题：分为3种情况
        #1、当2个节点都为左子树上的节点，或者都为右子树上的节点的时候，公共祖先为max(p,q)
        #2、当p,q一个在左子树，一个在右子树的时候，公共祖先就为根节点
        #3、当节点P，或Q为根节点的时候，就直接返是p或者q
        #解题：1、暴力求解，查到p和q向上回溯，碰到的一样的点，则为其公共祖先
        #2、递归求解
        if not root or root==p or root ==q:
            return root
        else:
            left=self.lowestCommonAncestor(root.left,p,q)
            right=self.lowestCommonAncestor(root.right,p,q)
        if not left:
            return right
        if not right:
            return left
        else:
            return root





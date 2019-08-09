---
title: 数据结构和算法-链表实战之K个一组反转链表
date: 2019-08-06 13:31:30
tags: 数据结构和算法 链表实战 K个一组反转链表 leetcode-25
---

## 链表实战题目5 - K个一组反转链表

给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 : 给定这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5

说明 : 你的算法只能使用常数的额外空间。你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

<!-- more -->

首先这里每组k个元素进行翻转，翻转之后每组需要进行衔接。例如[1, k]与[k+1,2k]之间的衔接。另外还需要注意剩余不到k个元素的处理。参考此[链接](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/python3-die-dai-di-gui-jian-yao-shuo-ming-by-leaco/)。

### 方法一：迭代法:借助单链表翻转

``` python
# Definition for singly-linked list.
# class ListNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.next = None

class Solution(object):
	def reverseKGroup(self, head, k):
		"""
		:type head: ListNode
		:type k: int
		:rtype: ListNode
		"""
		cur = head
		dim = ListNode(0)
		dim.next = head
		# pre为k个一组的头
		pre = dim
		count = 1
		while cur:
			# 每k个元素一组，对这里面的数据进行翻转
			if count % k == 0:
				# 后面的一个k个一组的头节点
				nextstart = cur.next
				# 前面的k个一组为新链表，以None结束
				cur.next = None
				# 反转新链表，返回翻转后的头和尾，pre.next为翻转前的头节点。
				end, start = self.reverseList(pre.next)
				
				""" 
				下面为衔接处理，pre前一个k个一组的尾节点
				end指向下一个k个一组的头节点
				现在的pre变为end
				cur变为nextstart
				"""
				pre.next, end.next, pre, cur = start, nextstart, end, nextstart
			else:
				cur = cur.next
			count += 1
		return dim.next

	def reverseList(self, head):
		temp, cur, pre = head, head, None
		while cur:
			cur.next, pre, cur  = pre, cur, cur.next
			# 以上的一句代码相当于如下的三句代码

			# 当前节点指向前一个节点。这里实际上就是反转列表的第一步，将当前节点指向pre节点，即前一个节点初始值None
			# cur.next = pre

			# 这里是将当前节点赋给pre, 也就是当前节点变为了前一个节点 
			# pre = cur

			# 当前节点往后移动
			# cur = cur.next
		return temp, pre
```

### 方法二：递归法

递归终止条件：剩余节点 < k。

递归从里向外出来，每层递归返回当前层级链表翻转后的头节点，那么每层递归中我们知道当前层级翻转后的头尾节点以及下一个k元素组的头节点（递归的上一层级），可以很轻松地将翻转后的链表衔接起来

``` python
class Solution(object):
	def reverseKGroup(self, head, k):
		"""
		:type head: ListNode
		:type k: int
		:rtype: ListNode
		"""
		if self.isEnd(head, k):
			return head
		pre = ListNode(None)
		pre.next, cur, count = head, head, 1

		# 反转k个一组链表
		while count <= k:
			cur.next, pre, cur, count = pre, cur, cur.next, count + 1
		
		# 循环结束后，cur指向下一组k个元素（未翻转）的头
		# pre指向当前组在翻转后的头节点
		# nexthead 下一组翻转后的头节点
		nexthead = self.reverseKGroup(cur, k)
		
		# 当前组的head在翻转后成为尾节点，其next指向nexthead 下一组翻转后的头节点
		head.next = nexthead
		
		# 返回翻转后的头节点
		return pre

	# 递归终止的判断条件
	def isEnd(self, head, k):
		count, cur = 0, head
		while cur:
			count += 1
			cur = cur.next
			if count >= k:
				return False

		return True
```

### 方法三：借助栈

将k个元素压入栈，通过出栈翻转，注意剩余元素处理。[参考这里](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/kge-yi-zu-fan-zhuan-lian-biao-by-powcai/)。

``` python
class Solution(object):
	def reverseKGroup(self, head, k):
		dummy = ListNode(0)
		p = dummy
		while True:
			count = k 
			stack = []
			tmp = head
			while count and tmp:
				stack.append(tmp)
				tmp = tmp.next
				count -= 1
			# 注意,目前tmp所在k+1位置
			# 说明剩下的链表不够k个,跳出循环
			if count : 
				p.next = head
				break
			# 翻转操作
			while stack:
				p.next = stack.pop()
				p = p.next
			#与剩下链表连接起来 
			p.next = tmp
			head = tmp
		return dummy.next
```

















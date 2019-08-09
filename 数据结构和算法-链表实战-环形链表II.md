---
title: 数据结构和算法-环形链表II
date: 2019-08-06 9:30:00
tags: 数据结构和算法 链表实战 环形链表 leetcode-142
---

## 链表实战题目4 -  链表入环的第一个节点

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
说明：不允许修改给定的链表。
进阶：你是否可以不用额外空间解决此题？

<!-- more -->

### 方法一：直接法：哈希表

此方法的空间复杂度为O(n)，并非最优，但是属于比较容易想到的方法。参考此[链接](https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/kuai-man-zhi-zhen-by-powcai-4/)。

``` python
class Solution(object):
	def detectCycle(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if not head or not head.next: return None
		
		visited = set()
		p = head
		
		while p:
			visited.add(p)
			# 如果成环，那么当前节点的下一个在已经遍历过的节点集合内
			if p.next in visited:
				# 返回这个下一个节点即可
				return p.next
			p = p.next
		return None
```

### 方法二：快慢指针法

使用一个快指针和一个慢指针，快指针每次都是走两步，慢指针每次都是走一步。如果二者可以相遇，即 fast == slow，那么代表链表中存在环。如果快指针走到了链表的尾部就会跳出循环，链表中无环。

当有环且快慢指针重合时，假设x为非环部分的长度，y为形成环路的位置到快慢指针重合位置的距离，z为快慢指针重合位置至形成环路位置之间的距离。重合时，慢指针行进的距离 = x + y；快指针行进的距离 = x + y + z + y。因为快指针的行走距离是慢指针的2倍，则有：2 * (x + y) = x + y + z + y。解得：x = z。

所以，通过在快慢指针重合的位置以及链表起始位置head，放置两个指针开始循环，每次两边各前进一个位置，当两者重合时的位置，就是链表形成环路的那个位置。参考此[链接](https://leetcode-cn.com/problems/linked-list-cycle/solution/bu-chong-ti-mu-qiu-xing-cheng-huan-de-ju-ti-wei-zh/)。


```python
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next : return 
        # 快慢指针
        slow = head
        fast = head
        # 重新开始
        start = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 找到相遇点
            if slow == fast:
                while slow != start:
                    slow = slow.next
                    start = start.next
                return slow
        return None
```
































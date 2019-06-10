# coding:utf-8
# 代码实现方法1：
def insert_sort(alist):
	n = len(alist)
	for j in range(1, n):
		# j = [1,2,3,n-1]
		# i 代表内层循环起始值
		i = j
		while i > 0:
			if alist[i] < alist[i-1]:
				alist[i], alist[i-1] = alist[i - 1], alist[i]
				i -= 1
			else:
				break
# 代码实现方法2:
def insert_sort(alist):
	n = len(alist)
	for j in range(1, n):
		# j = [1,2,3,n-1]
		# i 代表内层循环起始值
		for j in range(i, 0, -1): #  不包括0
			if alist[j] < alist[j-1]:
				alist[j], alist[j-1] = alist[j-1], alist[j]
 

if __name__ = "__main__":
	li = [2,34,56,24,12,78,54]
	print(li)
	insert_sort(li, 0, n-1)
	print(li)

# coding:utf-8
def shell_sort(alist):
	n = len(alist)
	gap = n//2 # python3
	while gap >= 1:
		# gap = 1时就是普通的插入排序
		# 代码和插入排序相似，区别就是gap步长
		for j in range(gap, n): # 某一个gap得到的所有子序列通过下面的代码一次性处理
			# j = [gap, gap+1, gap+2, gap+3, ..., n-1]
			i = j
			while i >= 0:
				if alist[i] < alist[i-gap]:
					alist[i],alist[i-gap] = alist[i-gap], alist[i]
					i -= gap
				else:
					break
		# 缩短gap步长
		gap //= 2

if __name__ = "__main__":
	li = [2,34,56,24,12,78,54]
	print(li)
	shell_sort(li, 0, n-1)
	print(li)

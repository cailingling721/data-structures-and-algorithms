# coding:utf-8

def select_sort(alist):	
	n = len(alist)
	for j in range(n-1):
		min_index = j
		for i in range(j, n):
			if alist[min_index] > alist[i]:
				min_index = i
		alist[min_index], alist[j] = alist[j], alist[min_index]

if __name__ = "__main__":
	li = [2,34,56,24,12,78,54]
	print(li)
	select_sort(li, 0, n-1)
	print(li)

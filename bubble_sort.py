# 方法1：
# coding:utf-8
def bubble_sort(alist):
	n = len(alist)
	for j in range(n-1):
		for i in range(0, n-1-j):
			# 让班长从头走到尾，i代表每次遍历需要比较的次数，是逐渐减小的
			if alist[i] > alist[i+1]:
				alist[i],alist[i+1] = alist[i+1],alist[i]
# i 0 ~ n-2 range(0, n-1) j = 0
# i 0 ~ n-3 range(0, n-1-1) j = 1
# i 0 ~ n-4 range(0, n-1-1-1) j = 2
# i 0 ~ n-1-j range(0, n-1-j) j = n
if __name__ = "__main__":
	li = [54,26, 93, 17, 77, 31,  44, 55, 20]
	bubble_sort(li)
	print(li)

# 方法2:
# coding:utf-8
def bubble_sort(alist):
	n = len(alist)
	for j in range(n-1,0,-1):
		for i in range(j):
			# 让班长从头走到尾，i代表每次遍历需要比较的次数，是逐渐减小的
			if alist[i] > alist[i+1]:
				alist[i],alist[i+1] = alist[i+1],alist[i]
# i 0 ~ n-2 range(0, n-1) j = 0
# i 0 ~ n-3 range(0, n-1-1) j = 1
# i 0 ~ n-4 range(0, n-1-1-1) j = 2
# i 0 ~ n-1-j range(0, n-1-j) j = n
if __name__ = "__main__":
	li = [54,26, 93, 17, 77, 31,  44, 55, 20]
	bubble_sort(li)
	print(li)

时间复杂度：
# coding:utf-8
def bubble_sort(alist):
	n = len(alist)
	for j in range(n-1):
		count = 0
		for i in range(0, n-1-j):
			# 让班长从头走到尾，i代表每次遍历需要比较的次数，是逐渐减小的
			if alist[i] > alist[i+1]:
				alist[i],alist[i+1] = alist[i+1],alist[i]
				count += 1
			if 0 == count:
				# 没有进行任何交换，直接退出
				break
 
 if __name__ = "__main__":
	li = [2,34,56,24,12,78,54]
	print(li)
	bubble_sort(li, 0, n-1)
	print(li)

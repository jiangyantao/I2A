#算法导论的第10页，插入排序，数组升序排列。
def insertion_sort_UP(A):
	for j in range(1,len(A)):
		key = A[j]
		i = j - 1
		while i>=0 and A[i]>key:
			A [i+1] = A[i]
			i = i-1
		A[i+1] = key
	return A

#算法导论的第10页，插入排序，数组降序排列。
def insertion_sort_DOWN(A):
	for j in range(1,len(A)):
		key = A[j]
		i = j - 1
		while i>=0 and A[i]<key:
			A [i+1] = A[i]
			i = i-1
		A[i+1] = key
	return A

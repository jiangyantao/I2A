def test2_1_3(A,v):
	for j in range(0,len(A)):
		if v == A[j]:
			return A[j]
	return 'NIL'

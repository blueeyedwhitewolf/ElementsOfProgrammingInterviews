def rotate_matrix(square_matrix: List[List[int]])->None:
	matrix_size=len(square_matrix)
	for i in range(len(square_matrix)//2):
		for j in range(i, matrix_size-i):
			#Perform a 4-way exchange. Note that A[~i] for i in [0,len(A)-1] is A[-(i+1)]
			(square_matrix[i][j], square_matrix[~j][i], square_matrix[~i][~j], square_matrix[j][~i])=(
				square_matrix[~j][i],
				square_matrix[~i][~j],
				square_matrix[j][~i],
				square_matrix[i][j]
				)
	#Time complexity is O(n^2) abd aditional space complexity O(1)

	
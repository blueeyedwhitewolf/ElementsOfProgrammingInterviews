 '''
 def matrix_in_spiral_order(square_matrix: List[List[int]])->List[int]:
 	def matrix_layer_in_clockwise(offset):
 		if offset==len(square_matrix)-offset-1:
 			#square matrix has odd dimension, and we are at the center of the matrix square_matrix
 			spiral_ordering.append(square_matrix[offset][offset])
 			return

 		spiral_ordering.extend(square_matrix[offset][offset:-1-offset])
 		spiral_ordering.extend(
 				list(zip(*square_matrix[-1-offset][-1-offset:offset:-1]))
 			)
 		spiral_ordering.extend(list(zip(*square_matrix))[offset][-1-offset:offset:-1])

 		spiral_ordering:List[int]=[]
 		for offset in range((len(square_matrix)+1//2)):
 			matrix_layer_in_clockwise(offset)

 		return spiral_ordering

 #Time complexity is O(n^2)
'''

def matrix_in_spiral_order(square_matrix:List[List[int]])->List[int]:
	shift=((0,1)(1,0),(0,-1),(-1,0))
	direction=x=y=0
	spiral_ordering=[]

	for _ in range(len(square_matrix)**2):
		spiral_ordering.append(square_matrix[x][y])
		netx_x, next_y=x+shift[direction][0] y+shift[direction][1]
		if(next_x not in range(len(square_matrix))
			or next_y not in range(len(square_matrix))
			or square_matrix[next_x][next_y]==0
			):
		direction=(direction+1)&3
		next_x, next_y=x+shift[direction][0],y+shift[direction][1]
		x,y=next_x, next_y
	return spiral_ordering
	
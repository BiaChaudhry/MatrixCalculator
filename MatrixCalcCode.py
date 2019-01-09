print("\n\t\t\t\t\t\t\t\t\t\tMatrix Calculator in Python 3")

print("Here you can Perform following operations on matrices:\n")

print("1.Addition of matrices\n2.subtraction of matrices\n3.Product of matrices\n4.Transpose of a matrix\n5.Determinant of 2X2 matrix")

def matrixDeterminant():                                   # function for Determinant of 2X2 matrix 
	
	matrix    = []

	MatrxRow  = int(input("Enter the number of rows:"))

	MatrxColumn = int(input("Enter the number of Columns:"))

	print("\t Original Matrix  \t")

	for i in range(MatrxRow):

		matrix.append([0]*(MatrxColumn))                             # printing an original matrix

	for j in range(MatrxRow):

		for k in range(MatrxColumn):

			matrix[j][k] = int(input("Element at row %d , column %d " % (j , k)))              # j is the number  of rows and k is the number of columns

	detMatrix = [[0 for y in range(len(matrix))]for x in range(len(matrix[0]))]              # generating an initial space for the resultant matrix

	for o in range(len(matrix)):

		for p in range(len(matrix[0])):

			detMatrix = (matrix[0][0] * matrix [1][1]) - (matrix[0][1] * matrix[1][0])       # Applying formula for the determinant of 2 by 2 matrix

	print("Original Matrix",matrix)

	print("Determinant of a matrix = ",detMatrix)



def matrixTrans():                                                #  function for Transpose of a matrix
	
	matrix    = []

	MatrxRow  = int(input("Enter the number of rows:"))

	MatrxColumn = int(input("Enter the number of Columns:"))

	print("\t Original Matrix  \t")

	for i in range(MatrxRow):

		matrix.append([0]*(MatrxColumn))

	for j in range(MatrxRow):

		for k in range(MatrxColumn):

			matrix[j][k] = int(input("Element at row %d , column %d " % (j , k)))

	transpose = [[0 for y in range(len(matrix))]for x in range(len(matrix[0]))]

	for l in range(len(matrix)):

		for m in range(len(matrix[0])):

			transpose[m][l] = matrix [l][m]

	print("Original matrix", matrix)

	print("Transpose of a Matrix",transpose)


def matrixMultiply(matrixA,matrixB):                                                  #  function for Product of matrices

	resultantMatrix = [[ 0 for y in range(len(matrixB[0]))]for x in range(len(matrixA))]

	for i in range(len(matrixA)):

		for j in range(len(matrixA)):

			for k in range(len(matrixA[0])):

				resultantMatrix[i][j] = matrixA[i][k] * matrixB [k][j]

	matrixPrint(matrixA,matrixB)

	print ("resultant Matrix :",resultantMatrix)


def matrixAddOrSub(matrixA,matrixB,operation):                                                      # function for Addition  and subtraction of matrices
	
	resultantMatrix = [[0 for y in range(len(matrixA[0]))] for x in range(len(matrixA))]            # generating an initial space for resultant matrix

	if operation == "+":

		for i in range(len(matrixA)):

			for j in range(len(matrixB)):

				resultantMatrix[i][j] = matrixA[i][j] + matrixB [i][j]

	elif operation == "-":

		for i in range(len(matrixA)):

			for j in range(len(matrixB)):

				resultantMatrix[i][j] = matrixA[i][j] - matrixB [i][j]

	matrixPrint(matrixA,matrixB)

	print("Resultant Matrix\n",resultantMatrix)


def matrixPrint(matrixA,matrixB):                                                            # function for printing matrices

	print("Matrix A\n",matrixA)

	print("Matrix B\n",matrixB)
	
def main():                                                                                  # main function

	matrixA = []

	matrixB = []

	operation = input("Enter the operation ('+' , '-' , 'X' , 'transpose' , 'determinant' )\n")

	if operation == '+' or operation ==  '-' or operation == 'X' or operation =="x":
	

		rowMatrxA = int(input("Enter the number of rows  of matrixA:"))

		columnMatrxA = int(input("Enter the number of columns  of matrixA:"))

		rowMatrxB = int(input("Enter the number of rows  of matrixB:"))

		columnMatrxB = int(input("Enter the number of columns  of matrixB:"))
	
		flag = True

		try:

			if operation == "+" or operation == "-":

				if rowMatrxA != rowMatrxB or columnMatrxA != columnMatrxB :        # Condition for subtraction or sum of the matrices

					raise ("exeption") 

			if operation == "X" or operation == "x": 

				if columnMatrxA != rowMatrxB :                                      # Condition for  the product of matrices

					raise ("exception")

					print("Matrix Multiplication is not possibe")
			
		except:

			print("Solution not Possible\n ")

			flag = False

		if flag:

			print("\t Matrix A \t")

			for i in range(rowMatrxA):

				matrixA.append([0]*(columnMatrxA))

			for j in range(rowMatrxA):

				for k in range(columnMatrxA):

					matrixA[j][k] = int(input("Element at row %d , column %d " % (j , k)))

			print("\t Matrix B \t")

			for i in range(rowMatrxB):

				matrixB.append([0]*(columnMatrxB))

			for j in range(rowMatrxB):

				for k in range(columnMatrxB):

					matrixB[j][k] = int(input("Element at row %d , column %d " % (j , k)))

			if operation == "+" or operation == "-":

				matrixAddOrSub(matrixA,matrixB,operation)

			elif operation == "X" or operation == "x":

				matrixMultiply(matrixA,matrixB)

	elif operation == "transpose":

		matrixTrans()

	elif operation == "determinant":

		matrixDeterminant()
main()





#This is a matrix calculator from Zuhayr, does not support augmented matrices. Please do not use for cheating purposes.
#import matrix

def create_matrix(m, n): #COMPLETE
    '''Initializes matrix, asks for series of inputs based on size of matrix'''
    matrix = []
    rows = []
    for row in range(1, m + 1):  # gets user input for matrix and initializes the matrix
        rows = []
        for val in range(1, n + 1):
            value = int(input('What value would you like to enter for this position? [' + str(row) + '] [' + str(val) + '] : '))
            rows.append(value)

        matrix.append(rows)
    return matrix

def get_n_columns(mat): #COMPLETE
    counter = 0
    rowCount = len(mat)
    for row in mat:
        for val in row:
            counter += 1
    return int(counter/rowCount)

def remove_column(mat, column):
    '''Removes the specified column from the inputted matrix'''
    for row in mat:
        for val in row:
            if row.index(val) == column - 1:
                row.pop(val)
    return mat

def rref(mat): #INCOMPLETE

    n_rows = len(mat)

    n_columns = get_n_columns(mat)
    for column in range(1, n_columns + 1):
        pass

def det(mat): #INCOMPLETE
    
    col = get_n_columns(mat)
    row = len(mat)
    if get_n_columns(mat) != len(mat): #case if the matrix is not square
        return 'Matrix is not square, cannot calculate determinant.'

    else: #matrix is square case
        while len(mat) != 2:#reduction of the matrix until it is 2 by 2
            for element in mat[0]:
                column = element.index()
                newmat = mat.pop(element)

        return det(newmat)



# MAIN PROGRAM
while True:
    try:
        i = int(input('Numbers of rows: '))  # will eventually be number of lists within the matrix list
        j = int(input('Number of columns: '))  # will be number of elements within each row list
        break
    except ValueError:
        print('That does not seem to be an integer, please enter an integer')


a = create_matrix(i, j)
print(a)
remove_column(a, 1)
print(a)
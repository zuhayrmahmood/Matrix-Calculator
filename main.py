#This is a matrix calculator from Zuhayr, does not support augmented matrix
#import matrix

def create_matrix(m, n):
    '''Initializes matrix, asks for series of inputs based on size of matrix'''
    matrix = []
    rows = []
    for row in range(1, m + 1):  # gets user input for matrix and initializes the matrix
        rows = []
        for val in range(1, n + 1):
            value = input('What value would you like to enter for this position? [' + str(row) + '] [' + str(val) + '] : ')
            rows.append(value)

        matrix.append(rows)
    return matrix

def rref(mat):
    n_columns = len(mat)
    for row in range(j):



# MAIN PROGRAM
while True:
    try:
        i = int(input('Numbers of rows: '))  # will eventually be number of lists within the matrix list
        j = int(input('Number of columns: '))  # will be number of elements within each row list
        break
    except ValueError:
        print('That does not seem to be an integer, please enter an integer')

print(create_matrix(i, j))
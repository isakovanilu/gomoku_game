
# arbitrary matrix sizes
# 1st version - H vs H

def update_matrix(matrix, row, column, value):
    row_len = len(matrix) # row length
    col_len = len(matrix[0]) # column lenght
    if (row >= row_len or column >= col_len) or matrix[row][column] != ' ': # if the coordinates greater than matrix size return the function
        print('Please enter different coordinates')
    else:
        for i in range(row_len): # loop throught rows
            for j in range(col_len): # loop throught columns
                if i == row and j == column: # if row and columns values match for the given coordinates
                    matrix[i][j] = value # assign the new values for those coordinates
    matrix_length = len(matrix)*4 - 3 # to ajust the horizontal line
    for row in matrix:
        print(" | ".join(row))
        print("-" * matrix_length )
    return matrix

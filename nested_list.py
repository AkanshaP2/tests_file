matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Element at row 2, column 1:", matrix[1][0])

matrix[0][2] = 10
print("Modified matrix:")
for row in matrix:
    print(row)

new_row = [11, 12, 13]
matrix.append(new_row)
print("Matrix after adding a new row:")
for row in matrix:
    print(row)

print("Iterating through the matrix:")
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()

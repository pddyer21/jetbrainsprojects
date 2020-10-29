import math

def getmatrix(rx):
    m = []
    for x in range(rx):
        rws = [float(n) for n in input().split()]
        m.append(rws)
    return m


def addmatrices(m1, m2):
    msum = []
    matsum = []
    for y in range(len(m1)):
        for z in range(len(m1[0])):
            msum.append(m1[y][z] + m2[y][z])
        matsum.append(msum)
        msum = []
    return matsum


def multiplymatrices(m1, m2):
    mprod = []
    matprod = []
    dotprod = 0
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                dotprod += m1[i][k] * m2[k][j]
            mprod.append(dotprod)
            dotprod = 0
        matprod.append(mprod)
        mprod = []
    return matprod


def scalarmultmatrix(m, s):
    matmultnum = []
    matmult = []
    for a in range(len(m)):
        for b in range(len(m[0])):
            matmult.append(s * m[a][b])
        matmultnum.append(matmult)
        matmult = []
    return matmultnum


def printmatrix(m):
    for i in range(len(m)):  # Iterate over the rows
        for j in range(len(m[0])):  # Iterate over the columns
            print(m[i][j] , end=" ")
        print()


def isnumber(v):
    try:
        value = int(v)
        return True
    except ValueError:
        return False


def tmaindiag(m):
    trow = []
    dresult = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            trow.append(0)
        dresult.append(trow)
        trow = []
    for x in range(len(m)):
        for y in range(len(m[0])):
            dresult[x][y] = m[y][x]
    return dresult


def tsidediag(m):
    trow = []
    tresult = []
    a = len(m) - 1
    b = len(m) - 1
    for x in range(len(m)):
        for y in range(len(m[0])):
            trow.append(m[a][b])
            a -= 1
        tresult.append(trow)
        trow = []
        a = len(m) - 1
        b -= 1
    return tresult


def tverticalline(m):
    trow = []
    tresult = []
    b = len(m) - 1
    for x in range(len(m)):
        for y in range(len(m[0])):
            trow.append(m[x][b])
            b -= 1
        tresult.append(trow)
        trow = []
        b = len(m) - 1
    return tresult


def thorizontalline(m):
    trow = []
    tresult = []
    a = len(m) - 1
    for x in range(len(m)):
        for y in range(len(m[0])):
            trow.append(m[a][y])
        tresult.append(trow)
        trow = []
        a -= 1
    return tresult


def getmatrixminor(m, rx, cx):
    return [rowx[:cx] + rowx[cx+1:] for rowx in (m[:rx]+m[rx+1:])]


def matdet(m):
    det = 0
    if len(m) == 1:
        return m[0][0]
    elif len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    elif len(m) > 2:
        detrow = 0
        for detcol in range(len(m)):
            det += ((-1) ** (detrow + detcol)) * m[detrow][detcol] * matdet(getmatrixminor(m, detrow, detcol))
    return det


def matrixinv(m, d):
    matofcof = []
    matofcofrow = []
    if len(m) == 1:
        return [1 / m[0]]
    elif len(m) == 2:
        matofcofrow = [m[1][1], (-1) * m[0][1]]
        matofcof.append(matofcofrow)
        matofcofrow = [(-1) * m[1][0], m[0][0]]
        matofcof.append(matofcofrow)
        return scalarmultmatrix(matofcof, 1/d)
    else:
        for i in range(len(m)):
            for j in range(len(m[0])):
                matofcofrow.append(((-1) ** (i + j + 2) * matdet(getmatrixminor(m, i, j))))
            matofcof.append(matofcofrow)
            matofcofrow = []
        adjointmatrix = tmaindiag(matofcof)
        return scalarmultmatrix(adjointmatrix, 1/d)


#########################################################


while True:
    print("1. Add Matrices \n2. Multiply matrix by a constant \n3. Multiply matrices \n4. Transpose matrix \n5. Calculate a determinant \n6. Inverse matrix \n0. Exit")
    choices = [0, 1, 2, 3, 4, 5, 6]
    choice = input("Your choice: ")
    if isnumber(choice):
        if int(choice) in choices:
            if int(choice) == 1:
                rw1, col1 = input("Enter size of first matrix:").split()
                rows1 = int(rw1)
                cols1 = int(col1)
                print("Enter first matrix:")
                matrix1 = getmatrix(rows1)

                rw2, col2 = input("Enter size of second matrix:").split()
                rows2 = int(rw2)
                cols2 = int(col2)
                print("Enter second matrix:")
                matrix2 = getmatrix(rows2)

                if rows1 != rows2 and cols1 != cols2:
                    print("The operation cannot be performed.")
                    continue
                else:
                    matrixsum = addmatrices(matrix1, matrix2)
                    print("The result is:")
                    printmatrix(matrixsum)
                    print()
            elif int(choice) == 2:
                row, col = input("Enter size of matrix:").split()
                print("Enter matrix:")
                matrix = getmatrix(int(row))
                const = input("Enter constant:")
                if isnumber(const):
                    result = scalarmultmatrix(matrix, int(const))
                    print("The result is:")
                    printmatrix(result)
                    print()
                else:
                    print("Invalid Entry. Please enter a number.")
                    continue
            elif int(choice) == 3:
                rw1, col1 = input("Enter size of first matrix: ").split()
                rows1 = int(rw1)
                cols1 = int(col1)
                print("Enter first matrix:")
                matrix1 = getmatrix(rows1)

                rw2, col2 = input("Enter size of second matrix:").split()
                rows2 = int(rw2)
                cols2 = int(col2)
                print("Enter second matrix:")
                matrix2 = getmatrix(rows2)

                if cols1 != rows2:
                    print("This operation cannot be performed")
                else:
                    result = multiplymatrices(matrix1, matrix2)
                    print("The result is:")
                    printmatrix(result)
                    print()
            elif int(choice) == 4:
                tchoices = [1, 2, 3, 4]
                while True:
                    print("1. Main diagonal \n2. Side diagonal \n3. Vertical line \n4. Horizontal line")
                    tchoice = input("Your choice: ")
                    if isnumber(tchoice):
                        if int(tchoice) in tchoices:
                            if int(tchoice) == 1:
                                r, c = input("Enter matrix size:").split()
                                if isnumber(int(r)) and isnumber(int(c)):
                                    row = int(r)
                                    col = int(c)
                                    print("Enter matrix:")
                                    matrix = getmatrix(row)
                                    tmat = tmaindiag(matrix)
                                    print("The result is:")
                                    printmatrix(tmat)
                                    break
                                else:
                                    print("Invalid entry. Please enter numbers.")
                                    continue
                            elif int(tchoice) == 2:
                                r, c = input("Enter matrix size:").split()
                                if isnumber(int(r)) and isnumber(int(c)):
                                    row = int(r)
                                    col = int(c)
                                    print("Enter matrix:")
                                    matrix = getmatrix(row)
                                    tmat = tsidediag(matrix)
                                    print("The result is:")
                                    printmatrix(tmat)
                                    break
                                else:
                                    print("Invalid entry. Please enter numbers.")
                                    continue
                            elif int(tchoice) == 3:
                                r, c = input("Enter matrix size:").split()
                                if isnumber(int(r)) and isnumber(int(c)):
                                    row = int(r)
                                    col = int(c)
                                    print("Enter matrix:")
                                    matrix = getmatrix(row)
                                    tmat = tverticalline(matrix)
                                    print("The result is:")
                                    printmatrix(tmat)
                                    break
                                else:
                                    print("Invalid entry. Please enter numbers.")
                                    continue
                            elif int(tchoice) == 4:
                                r, c = input("Enter matrix size:").split()
                                if isnumber(int(r)) and isnumber(int(c)):
                                    row = int(r)
                                    col = int(c)
                                    print("Enter matrix:")
                                    matrix = getmatrix(row)
                                    tmat = thorizontalline(matrix)
                                    print("The result is:")
                                    printmatrix(tmat)
                                    break
                                else:
                                    print("Invalid entry. Please enter numbers.")
                                    continue
                        else:
                            print("Invalid Entry. choice must be between 1 and 4 inclusive.")
                            continue
                    else:
                        print("Invalid entry. Please enter numbers.")
                        continue
            elif int(choice) == 5:
                rw, col = input("Enter matrix size: ").split()
                rows = int(rw)
                cols = int(col)
                if rows != cols:
                    print("Invalid size. Must be square matrix")
                    continue
                else:
                    print("Enter matrix:")
                    matrix = getmatrix(rows)
                    determinant = matdet(matrix)
                    print("The result is:")
                    print(determinant)
                    print()
            elif int(choice) == 6:
                rw, col = input("Enter matrix size: ").split()
                rows = int(rw)
                cols = int(col)
                if rows != cols:
                    print("Invalid size. Must be square matrix")
                    continue
                else:
                    print("Enter matrix:")
                    matrix = getmatrix(rows)
                    determinant = matdet(matrix)
                    if determinant == 0:
                        print("This matrix doesn't have an inverse.")
                        print()
                        continue
                    else:
                        inversemat = matrixinv(matrix, determinant)
                        print("The result is:")
                        printmatrix(inversemat)
                        print()
            elif int(choice) == 0:
                break
        else:
            print("Invalid entry. Enter a value between 0 and 3 inclusive.")
            continue

    else:
        print("Invalid choice. Please enter numbers.\n")

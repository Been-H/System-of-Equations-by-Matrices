from matrix_class import Matrix

#Get system from user input
def getSystem():
    print("How many variables is your system?")
    while True:
        try:
            lenSystem = int(input())
        except ValueError:
            print("Please enter a number for the length of your system")
        else:
            break
    i = -1
    system = []
    for j in range(lenSystem):
        new_row = []
        while i < lenSystem:
            print("Please enter a coefficient of your system")
            while True:
                try:
                    num = int(input())
                except ValueError:
                    print("Please enter a coefficient of your system that is a number")
                else:
                    break
            new_row.append(num)
            i += 1
        print("great")
        system.append(new_row)
        i = -1
    return system, lenSystem

#create the matrix from Matrix class from the user input
def createMatrix(system, lenSystem):
    rows = []
    columns = []
    for item in system:
        rows.append(item)
    for i in range(lenSystem + 1):
        column = []
        for item in system:
            column.append(item[i])
        columns.append(column)
    m = Matrix(rows, columns, lenSystem)
    return m

#solves the matrix down to reduced row echelon form
def solveMatrix(m):
    i = 0
    m.show()
    while i != m.lenSystem:
        m.make_first_c_one(i)
        m.show()
        j = 0
        while j < m.lenSystem:
            if j != i:
                m.make_zero(i, j)
                m.show()
            j += 1
        i += 1
        m.update_columns()
from funcs import getSystem, createMatrix, solveMatrix

system, lenSystem = getSystem()
m = createMatrix(system, lenSystem)
solveMatrix(m)



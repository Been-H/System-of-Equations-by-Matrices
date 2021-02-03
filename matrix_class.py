from math import *
from copy import deepcopy

class Matrix:

    def __init__(self, rows, columns, lenSystem):
        self.rows = rows
        self.columns = columns
        self.lenSystem = lenSystem

    #shows matrix in a more visually appealing way
    def show(self):
        for row in self.rows:
            i = 0
            for item in row:
                if i == self.lenSystem - 1:
                    print(item, "         ", '|', "        ", end="")
                else:
                    print(item, "         ", end="")
                i += 1
            print('\n')
        print('\n\n\n\n')

    # only rows being manipulated so columns needs to be updated each iteration
    def update_columns(self):
        columns = []
        for i in range(self.lenSystem + 1):
            column = []
            for row in self.rows:
                column.append(row[i])
            columns.append(column)
        self.columns = columns

    #adds two rows together
    #the fab parameter is for when passing in an artificial (fabricated) row (explained below)
    def add_rows(self, addtoInd, adderInd, fab=False):
        if not fab:
            for i in range(self.lenSystem + 1):
                self.rows[addtoInd][i] += self.rows[adderInd][i]
        else:
            i = 0
            while i <= self.lenSystem:
                self.rows[addtoInd][i] += adderInd[i]
                i += 1

    # subtracts two rows
    # the fab parameter is for when passing in an artificial (fabricated) row (explained below)
    def sub_rows(self, subfromInd, subberInd,fab=False):
        if not fab:
            for i in range(self.lenSystem + 1):
                self.rows[subfromInd][i] -= self.rows[subberInd][i]
        else:
            i = 0
            while i <= self.lenSystem:
                self.rows[subfromInd][i] -= subberInd[i]
                i += 1

    #makes correct item in row 1
    def make_first_c_one(self, ind):
        if self.columns[ind][ind] != 1:
            divide = self.rows[ind][ind]
            for i in range(self.lenSystem + 1):
                self.rows[ind][i] = self.rows[ind][i] / divide

    #makes the rest of the items in the row zero. This is where the fab parameter comes in
    def make_zero(self, column, ind):
        if self.columns[column][ind] == 0:
            pass
        else:
            distance = abs(self.columns[column][ind])
            #if distance is int we can for loop
            if isinstance(distance, int):
                if self.columns[column][ind] < 0:
                    for i in range(distance):
                        self.add_rows(ind, column)
                elif self.columns[column][ind] > 0:
                    for i in range(distance):
                        self.sub_rows(ind, column)
            #otherwise we make a copy of the row and multiply by the distance if it's a float.
            #We then use that as a "fabricated" row in the add or subtract
            else:
                if self.columns[column][ind] < 0:
                    newRow = deepcopy(self.rows[column])
                    for num in newRow:
                        i = newRow.index(num)
                        newRow[i] = num * distance
                    self.add_rows(ind, newRow, fab=True)
                elif self.columns[column][ind] > 0:
                    newRow = deepcopy(self.rows[column])
                    for num in newRow:
                        i = newRow.index(num)
                        newRow[i] = num * distance
                    self.sub_rows(ind, newRow, fab=True)

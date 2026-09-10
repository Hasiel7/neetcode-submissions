class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columnValues = defaultdict(list)
        boxes = defaultdict(list)

        for rowIndex, row in enumerate(board):           #iterate through every row
            rowValues = defaultdict(int)                #for every row, create new dict for values
            for columnIndex, columnValue in enumerate(row): #iterate through every column in row
                if columnValue == ".":
                    continue
                rowValues[columnValue] += 1                # add columnValue + 1
                if rowValues[columnValue] > 1:
                    return False
                columnValues[columnIndex] += [columnValue]
                boxes[(rowIndex // 3, columnIndex // 3)] += [columnValue]

        for key in columnValues:
            values = columnValues.get(key)
            if self.contains_duplicates(values):
                return False

        for key in boxes:
            values = boxes.get(key)
            if self.contains_duplicates(values):
                return False
        return True

    def contains_duplicates(self, column: List[int]) -> bool:
        columnSet = set(column)
        return len(columnSet) != len(column)

        


#iterate through every row, while iterating, have a dictionary for column values, if any value greater
#than 1, false
#iterate through every column. keep dictionary, if at anyu index there contains a duplicate, false
#for every box we keep a dictionary, for


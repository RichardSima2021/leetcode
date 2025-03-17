def generate(numRows):
    rows = [[1], [1,1]]
    if numRows == 1:
        return rows[0:1]
    elif numRows == 2:
        return rows

    for i in range(2, numRows):
        # i is the current row number being generated
        # rows[i-1] is used to generate it
        newRow = [1]
        prevRow = rows[i-1]
        for c in range(0, len(prevRow) - 1):
            newRow.append(prevRow[c] + prevRow[c + 1])
        newRow.append(1)
        rows.append(newRow)

    return rows

print(generate(5))
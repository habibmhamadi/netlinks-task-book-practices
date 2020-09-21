
def print_table(table):
    """Left jutifies all columns

    Args:
        table (list of list of strings)
    """   
    for i in range(len(table[0])):
        maxLen = 0
        for j in range(len(table)):
            if len(table[j][i])>maxLen:
                maxLen = len(table[j][i])
        for k in range(len(table)):
            table[k][i] = table[k][i].ljust(maxLen)
    print('\n********All columns are left justified********\n')
    for i in table:
        row = ''
        for j in i:
            row+=j+'  '
        print(row.strip())
        
print_table([['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']])
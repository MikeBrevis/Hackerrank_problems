# STDIN      Function
# -----      --------
# 3          arr[][] sizes n = 3, m = 3
# 11 2 4     arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
# 4 5 6
# 10 8 -12

def diagonalDifference(arr):

    sum_values = []
    rest_values = []

    i = 0
    l = -1

    while i < len(arr):

        sum_values.append(arr[i][i])
        rest_values.append(arr[i][l])
        
        i += 1
        l -= 1

    absolute_difference = abs(sum(sum_values) - sum(rest_values))
    return absolute_difference

ref = diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]])
print(ref)


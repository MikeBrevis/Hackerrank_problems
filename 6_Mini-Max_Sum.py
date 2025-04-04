arr = [7, 69, 2, 221, 8974]
both_sum = []

max = max(arr)
min = min(arr)

both_sum.append(str(sum(arr) - max))
both_sum.append(str(sum(arr) - min))

result = (" ".join(both_sum))

print(result)




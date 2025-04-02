
def plusMinus(arr):

    total_numbers = len(arr) 
    zero_total = 0
    positive_num = 0
    negative_num = 0

    for i in arr:
        if i == 0:
            zero_total += 1
        elif i > 0:
            positive_num += 1
        else:
            negative_num += 1

    positive_pro = "{:.6f}".format(positive_num / total_numbers)
    negative_pro = "{:.6f}".format(negative_num / total_numbers)
    zero_pro = "{:.6f}".format(zero_total / total_numbers)

    final_print = f"{positive_pro}\n{negative_pro}\n{zero_pro}"

    print(final_print)

numbers = plusMinus([0, 0, -1, 1, 1])
print(numbers)


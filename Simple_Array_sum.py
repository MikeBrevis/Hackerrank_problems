#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Write your code here
    sum_all = 0
    
    for i in ar:
        sum_all += i
    return sum_all  

ar_count = int(input().strip()) 

ar = list(map(int, input().rstrip().split()))

result = simpleArraySum(ar)

print(result)





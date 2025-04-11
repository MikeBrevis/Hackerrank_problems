x1 = 14
v1 = 4
x2 = 98
v2 = 2

i = 1

while i < 10000:

    kangaroo_1 = x1 + (v1 * i)
    print(kangaroo_1)
    kangaroo_2 = x2 + (v2 * i)
    print(kangaroo_2)
        
    if kangaroo_1 == kangaroo_2:
        same_place = "YES"
        break

    else:
        same_place = "NO"

    i += 1
                
print(same_place)
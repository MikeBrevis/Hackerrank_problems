a = [17, 28, 30]
b = [99, 16, 8]

n = len(a)

alice = 0
bob = 0

for i in range(n) :
    if a[i] == b[i]:
        pass

    elif a[i] > b[i]:
        alice += 1

    else:
        bob += 1


print(alice,bob)


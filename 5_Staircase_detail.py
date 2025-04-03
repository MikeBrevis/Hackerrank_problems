n = 6
i = 1
space = n - 1
elements = []

while i <= n: 
    text = f"{" " * space}{"#" * i}"
    elements.append(text)
    i += 1
    space -= 1

tree = ("\n".join(elements))

print(tree)

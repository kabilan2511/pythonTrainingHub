numbers = {10, 20}

print(type(numbers))

numbers.update([30, 40])

print(numbers)

#add a element in set

numbers.add(50)

print(numbers)

#mathematical operations on sets

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union = a.union(b)  

print("Union of a and b:", union)
print(a.intersection(b))

#pop in sets

print("Popped element:", numbers.pop())

#in and no it

fruits = {"apple", "banana", "orange"}

if "banana" not in fruits:
    print("Not Found")
else:
    print("Found")
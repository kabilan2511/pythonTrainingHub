# tuples

student = "Anu", 21, "Python"
numbers = (10, 20, 30, 40, 50, 60, 20, 20)

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::2])
print(numbers[::-1])

first, *middle,last = numbers

print("##",first, middle, last)
# print(student)
# print(type(student))

#tuple do no provide methos to add

# numbers.append(70) # this will give error

student = ("Kab", 27, 85.5, True)

print(type(student));


# unpacking a tuple

student = ("Rahul", 22, "Bengaluru")

name, age, city = student

print(name)
print(age)
print(city)


# counting the number of occurences of a value in a tuple

count = numbers.count(20)
print("Count of 20 in tuple:", count)


#second largest number

sort_num = sorted(numbers)

print("Sorted numbers:", sort_num[-2])
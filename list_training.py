import copy


numbers = [1,2,3,9,5,6,7,8]

print(max(numbers))

large = 0;

for num in numbers:
    if(num > large):
       large = num

print("largest number is:", large)

#finding even and odd numbers

even = 0;
odd = 0;

for num in numbers:
    if(num % 2 == 0):
        even += 1
        print(num,"is even")
    else:
        odd += 1
        print(num,"is odd")

print("Total even numbers:", even)
print("Total odd numbers:", odd)


#reverse a string

reverse = numbers[::-1];

print("Reversed list is:", reverse)


# shalloow copy of a list

copy_list = numbers.copy()

print("Original list:", numbers)
print("Copied list:", copy_list)


# deep copy of a list

deep_copy_list = numbers[:]
deep_copy = copy.deepcopy(numbers)

print("Deep copy of a list:", deep_copy_list)
print("Deep copy of a list:", deep_copy)




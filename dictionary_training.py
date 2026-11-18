
profile = {
    "name" : "Kabilan",
    "age" : "27",  
    "city" : "Bengaluru",
    "skills" : ["python", "Js", "Html", "Css"]
}

print(profile["skills"][0])
print(profile.get("not_exist", "Key not found"))

# Remove duplicates from a list

numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9]

unique_numbers = list(set(numbers))

print(unique_numbers)
# print(max(unique_numbers))

#working on list

name = "Kabilan"

chars = list(name)

print(chars)

print(list("India")) 

print(list([1, 2, 3]))


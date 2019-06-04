# collections are of 3 types
# 1. List
# 2. Set - same as list, but no dupplicates
# 3. Dictionary - contains list with key, value pair

str1 = "  this is first string  "
print(str1)

str2 = "this is second string"

print(len(str1))

# indexing
print(str1[10])

# repetition
print(str1*3)

# slicing
print(str2[0:10])
print(str1[0:])
print(str2[:9])
print(str1[-3:-10])

# step in slicing

print(str1[0:19:3])
print(str1[20::-2])

# stripping spaces, string, lstrip, rstrip
print(str1.strip())

# find string
print(str1.find("first"))
print(str1.find("first", 0, 8))

# count occurrences
print(str1.count("is"))

# replace string
print(str1.replace("is", "XX", 1))

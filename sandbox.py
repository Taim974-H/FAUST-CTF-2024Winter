# groceries = {
#     'healthy': (['apple', 'banana'],['tomato','carrot']),
#     'unhealthy': 'chocolate'
#     }
# for i in groceries:
#     print(i, groceries[i])
#     print('0000')


# l = [1, 2, 3, 4, 5, 6]
#in python, list slicing is done by using the colon operator(:)
#syntax: l[start:stop:step], the start index is included, the stop index is not included.
# index starts from 0 and the step is the number of elements to skip.
# l[1:3]
# [2, 3]
# l[1:5:2]
# [2, 4]
# l[5:1:-1]
# [6, 5, 4, 3]
# l[::-1]
# [6, 5, 4, 3, 2, 1]

# • len(x): Returns the length of list, tuple, dictionary, ...
# • list(x): Converts iterable to list
# • ord(c)/chr(i): Converts character to/from unicode number
# • map(f, x): Applies f to every element of x and returns a new
# collection
# • x.sort(): Sorts list x
# • dir(x): Returns a list of all methods/variables of object/type
# x
# • x.join(y): Concatenates all elements in y with string x as
# separator

# def reversestr(s):
#     return s[::-1]
# f = ["Hello", "World", "Test"]
# f = list(map(reversestr, f))
# print(f)

# list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list(range(0, 10, 2))
# [0, 2, 4, 6, 8]
# list(range(9,0,-1))
# [9, 8, 7, 6, 5, 4, 3, 2, 1]

# f = open("file","w") # open file for writing, creates file if it does not exist
# f.write("Hello!\n")
# f.close()
# f = open("file","a")
# f.write("World\n")
# f.close()
# f = open("file","r")
# f.read(3)
# f.seek(0)
# f.readlines()
# # ['Hello!\n','World\n']


import hashlib

print(hashlib.md5(b"Hello World").hexdigest()) # hexdigest() returns the hash as a 32-character hexadecimal string
print(hashlib.sha256(b"Hello World").hexdigest()) # sha256() returns the hash as a 64-character hexadecimal string

import urllib
#example usage:
urllib.request.urlopen("http://www.google.com").read()



# extract all the lines that start with "aa" or end with "ee", join them, and compute the MD5 sum of the result.
# Keywords: open, readlines, (map, join, filter)

with open("fileflag2.txt", "r") as f:
    lines = f.readlines()


def myFunc(line):
  if line.strip().startswith("aa") or line.strip().endswith("ee"):
    return line
  
# print(lines)
print("========================================")
filteredlines = list(filter(myFunc, lines))
print(filteredlines)
# filtered_lines = list(filter(lambda line: line.strip().startswith("aa") or line.strip().endswith("ee"), lines))
# print(filtered_lines)
sorted_lines = ''.join(sorted(line.strip() for line in filteredlines))
print("========================================")
import hashlib
flag = hashlib.md5(sorted_lines.encode()).hexdigest()
print(flag)




# filtered_lines = list(filter(lambda x: x.startswith("aa") or x.endswith("ee"), lines))
# print(filtered_lines)
# sorted_lines = ''.join(sorted(line.strip() for line in filtered_lines))
# print(sorted_lines)

# flaglines = []
# for line in lines:
#     if line.startswith("aa") or line.endswith("ee"):
#         flaglines.append(line)
#         # print(line)
# print("========")
# print(flaglines)
# sorted_lines = ''.join(sorted(line.strip() for line in flaglines))
# print(sorted_lines)
# import hashlib
# print("========")
# flag = hashlib.md5(sorted_lines.encode()).hexdigest()
# print(flag)
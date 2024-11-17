with open("fileflag1.txt", "r") as f:
    lines = f.readlines()

print(lines)
print("========")
sorted_lines = ''.join(sorted(line.strip() for line in lines)) # for every line in lines, strip the line and sort it - joining the lines after
print(sorted_lines)
print("========")
import hashlib
flag = hashlib.md5(sorted_lines.encode()).hexdigest()
print(flag)

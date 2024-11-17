# We have obtained part of the admin's password. 
# Unfortunately we could only get the first 35 digits of the password out of a total of 40. 
# We know that the SHA1
# sum of the password is fd8b6b5944fcede476bd62989044bd0fa36400e8 and that the first 35 digits are 36979765629224074726367327745686243.

sumofpasswordSHA1 = "fd8b6b5944fcede476bd62989044bd0fa36400e8"
first35digits = 36979765629224074726367327745686243
first35digits_str = str(first35digits)

password = ""
interations = 5
import hashlib
for i in range(99999999): 
    suffix = f"{i:05d}" # this means that the suffix will be a 5 digit number ( we are only missing 5 digits)
    password = first35digits_str + suffix 
    if hashlib.sha1(password.encode()).hexdigest() == sumofpasswordSHA1:
        print("Password found!")
        print(password)
        break

flag = hashlib.md5(password.encode()).hexdigest()
print(flag)


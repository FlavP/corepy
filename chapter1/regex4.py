import re

#or and pipes

# randStr = "1. Dog 2. Cat 3. Turtle"
# regex = re.compile(r"\d+\.\s(Dog|Cat)")
# matches = re.findall(regex, randStr)
# for i in matches:
#     print(i)

randStr = "12345 12345-1234 1234 13543-222"
regex = re.compile(r"\d{5}\s|\d{5}\-\d{4}\s")
matches = re.findall(regex, randStr)
for i in matches:
    print(i)
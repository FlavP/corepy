import re

#or and pipes

# randStr = "1. Dog 2. Cat 3. Turtle"
# regex = re.compile(r"\d+\.\s(Dog|Cat)")
# matches = re.findall(regex, randStr)
# for i in matches:
#     print(i)

# randStr = "12345 12345-1234 1234 13543-222"
# regex = re.compile(r"\d{5}\s|\d{5}\-\d{4}\s")
# matches = re.findall(regex, randStr)
# for i in matches:
#     print(i)
#group
# bd = input("Enter your birthday (mm-dd-yyyy) : ")
#
# bdRegex = re.search(r"(\d{1,2})-(\d{1,2})-(\d{4})", bd)
# print("You were born on", bdRegex.group())
# print("Your birth Month", bdRegex.group(1))
# print("Your birth Year", bdRegex.group(2))
# print("Your birth Day", bdRegex.group(3))
#named group
# randStr = "December 21 1974"
# regex = r"^(?P<month>\w+)\s(?P<day>\d+)\s(?P<year>\d{4})"
# matches = re.search(regex, randStr)
# print("Month :", matches.group('month'))
# print("Day :", matches.group('day'))
# print("Year :", matches.group('year'))

# randStr = "d+b@aol.com a_1@yahoo.co.uk A-100@m-b.INTERNATIONAL"
# regex = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.+-]+\.[a-zA-Z0-9_.+-]+")
# matches = re.findall(regex, randStr)
# for i in matches:
#     print(i)

randStr = "14125551212 4125551212 (412)5551212 412 555 1212 412-555-1212 1-412-555-1212"
regex = re.compile(r"((1?)(-| ?)(\()?(\d{3})(\)|-| |\) )?(\d{3})(-| )?(\d{4}|\d{4}) )")
matches = re.findall(regex, randStr)
for i in matches:
    print(i[0].lstrip())
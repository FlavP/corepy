import re

# randStr = "cat cats"
# regex = re.compile("[cta]+s?")
# matches = re.findall(regex, randStr)
# for i in matches:
#     print(i)
# randStr = "doctor doctors doctor's "
# regex = re.compile("[doctor]+['s]*")
# matches = re.findall(regex, randStr)
# for i in matches:
#     print(i)

# randStr = '''Just some words
# and some more\r
# and more
# '''
# thePattern = "[\w\s]+[\r]?\n"
# matches = re.findall(thePattern, randStr)
# print("Matches :", len(matches))
# for i in matches:
#     print(i)
# randStr = "<name>Life on Mars</name><name>Freaks and Geeks</name>"
# thePattern = "<name>(.*?)</name>"
# matches = re.findall(thePattern, randStr)
# print("Matches :", len(matches))
# for i in matches:
#     print(i)
# randStr = "ape at the apex"
# regex = re.compile(r"\bape\b")
# matches = re.findall(regex, randStr)
# print("Matches :", len(matches))
# for i in matches:
#     print(i)
# randStr = "Match everything up to @"
# regex = re.compile(r"^.*[^@]")
# matches = re.findall(regex, randStr)
# print("Matches :", len(matches))
# for i in matches:
#     print(i)
# randStr = "@ Get the string"
# regex = re.compile(r"[^@\s].*$")
# matches = re.findall(regex, randStr)
# print("Matches :", len(matches))
# for i in matches:
#     print(i)
# randStr = '''Ape is big
# Turtle is slow
# Cheetah is fast
# '''
#
# regex = re.compile(r"(?m)^.*?\s")
# matches = re.findall(regex, randStr)
# print("Matches :", len(matches))
# for i in matches:
#     print(i)

# randStr = "My number is 412-555-1212"
#
# regex = re.compile(r"412-(.*)")
# matches = re.findall(regex, randStr)
# print("Matches :", len(matches))
# for i in matches:
#     print(i)

# randStr = "412-555-1212 412-555-1213 412-555-1214"
#
# regex = re.compile(r"412-(.{8})")
# matches = re.findall(regex, randStr)
# print("Matches :", len(matches))
# for i in matches:
#     print(i)

randStr = "My number is 412-555-1214"

regex = re.compile(r"412-(.*)-(.*)")
matches = re.findall(regex, randStr)
print("Matches :", len(matches))
print(matches[0][0])
print(matches[0][1])
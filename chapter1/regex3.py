import re

#back references allows us to reuse the expression that preceeds it

# randStr = "the cat cat fell out the windows"
# regex = re.compile(r"(\b\w+)\s+\1")
#
# matches = re.findall(regex, randStr)
# print("Matches: ", len(matches))
# for i in matches:
#     print(i)
#cam ce am eu nevoie (faci match pe expresie, bagi o subexpresie care ia fix textul pe care il doream, apoi inlocuiesti
#expresia initiala sau textul initial cu expresia izolata )
# randStr = "<a href='#'><b>The Link</b></a>"
# regex = re.compile(r"<b>(.*?)</b>")
# randStr = re.sub(regex, r"\1", randStr)
# print(randStr)
# randStr = "412-555-1212"
# regex = re.compile(r"([\d]{3})-([\d]{3}-[\d]{4})")
# randStr = re.sub(regex, r"(\1)\2", randStr)
# print(randStr)
# randStr = "https://www.youtube.com http://www.google.com"
# regex = re.compile(r"(https?://([\w.]+))")
# randStr = re.sub(regex, r"<a href='\1'>\2</a>\n", randStr)
# print(randStr)

# lookahead is a pattern to match, but not return
# (?=expression)

#randStr = "One two three four"
#we want the letters and numbers, but not the spaces
# regex = re.compile(r"\w+(?=\b)")
# matches = re.findall(regex, randStr)
# for i in matches:
#     print(i)

#the look behind (?<=expression)
# randStr = "1. Bread 2. Apples 3. Lettuce"
# regex = re.compile(r"(?<=\d.\s)\w+")
# matches = re.findall(regex, randStr)
# for i in matches:
#     print(i)

# randStr = "<h1>I am important</h1> <h1>So am I</h1>"
# regex = re.compile(r"(?<=<h1>).+?(?=</h1>)")
# matches = re.findall(regex, randStr)
# for i in matches:
#     print(i)
#Negative lookahead/lookbehind (text that does not match pattern)
#Negative lookahead (?!expression)
#Negative lookbehind (?<!expression)
randStr = "8 Apples $3, 1 Bread $1, 1 Cereal $4"
regex = re.compile(r"(?<!\$)\d+")
matches = re.findall(regex, randStr)

for i in matches:
    print(i)
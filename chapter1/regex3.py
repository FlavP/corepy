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
randStr = "https://www.youtube.com https://www.google.com"
regex = re.compile()

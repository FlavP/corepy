import re

# bri = 'tzuika'
# pattern = '[w]{4}'
# m = re.findall(pattern, bri)
# for i in m:
#     print(i)
# m = re.compile(pattern)
# if m is not None:
#     hm = m.sub("whisk", bri)
#     print(hm)

# theStr = "F.B.I N.S.A C.IA"
# thePattern = '.\..\..'
# m = re.findall(thePattern, theStr)
# for i in m:
#     print(i)

# theStr = '''This is
# a long string
# that goes for many lines
# '''
#print(theStr)

# regex = re.compile("\n")
# theStr = regex.sub(" ", theStr)
# print(theStr)

# randStr = '12345'
# print("Number of matches {}".format(len(re.findall("\d{1}", randStr))))

theStr = 'gigimarga@gmail.com'
thePattern = '\w{2,20}\@\w{2,20}\.\w{3}'
m = re.search(thePattern, theStr)
if m is not None:
    print("Am gasit patternul")
else:
    print("No such luck")
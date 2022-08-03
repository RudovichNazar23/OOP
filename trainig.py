import string

def contains_whitespace(s):
    return True in [c in s for c in string.whitespace]

xd = "Helloworld"

res = contains_whitespace(xd)
print(res)
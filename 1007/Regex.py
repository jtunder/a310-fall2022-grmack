import re 

one = re.compile("(\d)(\d)", re.VERBOSE)

print(one.sub(r"\2\1", "123"))


piglatin = re.compile("([BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz])([AEIOUaeiou])(\w*)")

pattern = "([BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz])([AEIOUaeiou])(\w*)"

inpt = "Happy"

# if re.match(pattern, inpt):
#     print(piglatin.sub(r"\2\3\1ay", inpt))
    # print("It matches!")


constantvowel = "([BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz])([AEIOUaeiou])(\w*)"
constantconstant = "([BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz])([BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz])(\w*)"
vowel = "([AEIOUaeiou])(\w*)"

constantregex = re.compile(constantconstant, re.VERBOSE)

inpt = "Child"
if re.match(constantconstant, inpt):
    print(constantregex.sub(r"\3\1\2ay", inpt))

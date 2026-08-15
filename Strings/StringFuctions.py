S1 = 'Data'
S2 = 'Science'
S3 = "  ###Machine@@    "
S4 = "Hello-Sir-How-Are-You"
S5 = ['Hello', 'Mam']
str = "my name is vinay saini"

# lowercase
lowerstr = S1.lower()
print(f"lower case of S1 : {lowerstr}")

# Upppercase
upperstr = S1.upper()
print(f"Upper case of S1 : {upperstr}")

# strip : removing extra spaces from starting and ending
stripedstr = S3.strip().strip('#').strip('@')
print(f"stripped S3 : {stripedstr}")

# replace
new_S2 = S2.replace('Science','Analysis')
print(f"updated S2 : {new_S2}")

# splitting based on '-'
sptdata = S4.split('-')
print(f"Splitted S4 : {sptdata}")

# join
joined = ' '.join(S5)
print(f"Joined S5 : {joined}")

# ------------------------------------------------

# title
titled = str.title()
print(f"Titled str : {titled}")

# capitalize
cap = str.capitalize()
print(f"Capitalized str : {cap}")

# swapcase
swapc = str.swapcase()
print(f"SwapeCased str : {swapc}")

# find
ind = str.find('is')
print(f"Index of is : {ind}")

# startswith
sw = str.startswith('my')
print(f"str starts with 'my' : {sw}")

# islower
il = str.islower()
print(f"str is in lowercase : {il}")

# isalpha : all are alphbates
ia = str.isalpha()
print(f"In str all are alpha : {ia}")

# len
length = len(str)
print(f"Len of str : {length}")

# count
cou = str.count('a')
print(f"'a' comes {cou} times in str")
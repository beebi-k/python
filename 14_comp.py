# separate vowels and consonants in string "hi hello raju"

s = "hi hello raju"

v = [val for val in s if val in "aeiou"]
c = [val for val in s if val != " " and val not in "aeiou"]

print(v)
print(c)

# vow =[]
# con=[]
# l=[vow.append(i) if i in ['a','e','i','o','u'] else con.append(i) for i in s if i!=' ']
# print(vow)
# print(con)

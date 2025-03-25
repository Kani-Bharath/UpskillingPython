#Strings work similar to arrays

s = "abc"
print(s[0:2])

#But they are immutable
#s[0]= "A"
s += "def" #creates new string
print(s)

#Valid numeric strings can be converted
print(int("123")+int("123"))

#And numbers can be converted to strings.It appends
print(str(123)+str(123))

#ASCII value
print(ord("a"))

#Combine a list of strings (with an empty string delimiter)

strings =["ab","cd", "ef"]
print(" ".join(strings))








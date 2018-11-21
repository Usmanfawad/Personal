print("Encryption via translating a string")

a = "aeiou"
b = "12345"
c= str.maketrans(a, b)

str= " i study in uit"

print(str.translate(c))

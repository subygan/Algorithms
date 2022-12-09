value = {
    "A" : 1,
    "a" : "hi",
    "aB" : "this",
    "AB" : "hey"
}

print(value["AB"])

m = [1,2,3,4,5,4,3,3,2]

print(value.get("A",1))
z = value.get("A",0)+1
print(z)

print(m[2:])

for i in m:
    print(i)
    if i>5:
        break


for i in range(len(m)):
    print(i)
print('a'<'b')

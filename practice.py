# ------------List
myList = [3, 5, 4, 7, 9, "Hello", -19]
print(myList)

x = list(range(10))
print(x)

y = list(range(1, 11))
print(y)

z = list(range(0, 101, 10))
print(z)
print(z[3])
print(z[-10])

# ------------Slicing
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

a = letters[:]
b = letters[3:]
c = letters[:8]
d = letters[2:9]
e = letters[1:10:2]
f = letters[::2]
g = letters[::-1]
h = letters[1:8:-1]
i = letters[7:0:-1]

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)

# ------------Tuples - Immutable List

t1 = (43, 45, 47)

print(t1)

# ------------Function

pack = list(range(21, 31))
pack_len = len(pack)
pack_max = max(pack)
pack_mim = min(pack)

print(pack)
print(pack_len)
print(pack_max)
print(pack_mim)

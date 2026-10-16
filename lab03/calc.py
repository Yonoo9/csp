a = int(input())
b = int(input())

def sm(a, b):
    return a + b
def vc(a, b):
    return a - b
def mp(a, b):
    return a * b
def dl(a, b):
    if b != 0:
        return a // b
    else:
        print('Error. Division by 0')

s = sm(a, b)
v = vc(a, b)
m = mp(a, b)
d = dl(a, b)

print(s)
print(v)
print(m)
print(d)
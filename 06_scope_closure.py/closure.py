def myFirstFunc(num):
    def inner(x):
        return x**num
    return inner

f = myFirstFunc(2)
g = myFirstFunc(3)

# print(f)
# print(g)
print(f(3))
print(g(3))
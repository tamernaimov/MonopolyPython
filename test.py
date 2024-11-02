import contextlib
import io
def testMethod():
    print("COOL")
    return 3

with io.StringIO() as buf, contextlib.redirect_stdout(buf):
    num = testMethod()

# Print only the returned value
print(num)
print('bruh')

print()
print()
print()
num = testMethod()
print(testMethod())
print()
print()

def returnExample():
    a = 7
    b = 4
    return a+b

c = returnExample()
print(c)
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

num = testMethod()

print("EXAMPLE OF DECORATORS")

def decorator1(func):
    def wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return wrapper

@decorator1
def call_name(name):
    print("The name is " + name)

#call_name = decorator1(call_name)

call_name("Poonam")

print("EXAMPLE OF GENERATORS")


def sum1(num):
    sum_res = 0
    for i in range(1, num):
        sum_res = sum_res + i
        yield i

    print('the sum is ' + str(sum_res))

print('Numbers being added are')

for num in sum1(10):
    print(str(num) )




print("EXAMPLE OF CONTEXT MANAGER")


class ContextManager():
    def __init__(self):
        print('initialisation')

    def __enter__(self):
        print('method enter')
        return self

    def __exit__(self, type1 , value, traceback):
        print('method exit')


with ContextManager() as manager:
    print('call of with statement')
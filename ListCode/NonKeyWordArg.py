
def multiply(*num):
    mul = 1
    for n in num:
        mul = mul * n
        yield n
    print("Multiplication is", mul)

print("Number being multiplies are")
for n in multiply(1, 30 , 10):
    print(n)








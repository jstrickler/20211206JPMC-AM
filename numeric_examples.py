
# int float
# WE DON'T CARE: bool complex

i1 = 123
i2 = 0b1001000101
i3 = 0xDeadBeef

print(i1, i2, i3)

print(0xDeadBeef + 1, '\n')

a = 19
b = 5

print(a + b, a - b, a * b)
print(a / b, a // b, a // -b)   # // is floored division
print(a ** b, a % b)  # power, modulus

x = 5
x *= 3   # x = x * 3
x += 10
x /= 5
print(x)

#  x++

a = "123"
b = 456
print(a + str(b))
print(int(a) + b)

# int float bool str list tuple dict

d = "DeadBeef"
print(int(d, 16))









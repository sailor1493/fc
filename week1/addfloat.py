from decimal import Decimal

# Named Constant
N = 10

# Repeat addition functionality
def repeat_addition(mem, step, reps):
    for i in range(reps):
        mem += step
    return mem

# IEEE 754 decimal64 Implementation (Ver. 2008)
mem = Decimal('0')
step = Decimal('0.1')

mem = repeat_addition(mem, step, N)

print("What we expect")
print("mem == 1")
print(mem == 1)

# IEEE 754 Double Precision Implementation
step = 0.1
mem = 0

mem = repeat_addition(mem, step, N)

print("What we get")
print("mem == 1")
print(mem == 1)

# A realistic alternative: calculate difference and compare it with epsilon
epsilon = 10e-6

print("A realistic alternative")
print("mem ~= 1?")
diff = mem - 1

if (-epsilon < diff and diff < epsilon):
    print(True)
else:
    print(False)
from decimal import *

mem = Decimal('0')
step = Decimal('0.1')

mem += step
mem += step
mem += step
mem += step
mem += step
mem += step
mem += step
mem += step
mem += step
mem += step

print("What we expect")
print("mem == 1")
print(mem == 1)

step = 0.1
mem = 0

mem += step
mem += step
mem += step
mem += step
mem += step
mem += step
mem += step
mem += step
mem += step
mem += step

print("What we get")
print("mem == 1")
print(mem == 1)

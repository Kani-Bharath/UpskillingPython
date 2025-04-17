n, m, z = 0.125, "abc", False

n = n + 1
n += 1 

n = 4
n = None
print(n)
n = 4

if n > 2:
     n -= 1
elif n == 2:
     n *= 2
else:
     n += 2

if((n > 2 and n != m) or n == m):
     n += 1

while n < 5:
     print(n)
     n += 1

for i in range(5):
     print(i)

for i in range(2,6):
     print(i)

for i in range (5,1,-1):
     print(i)

print(5 / 2)
print(5 // 2)
print(-3 // 2)
print(int(-3 / 2))

print(10 % 3)

print(-10 % 3)

import math
print(math.fmod(-10,3))
print(math.floor(3/2))
print(math.ceil(3/2))
print(math.sqrt(2))
print(math.pow(2,3))

#Max / Min Int

float("inf")
float("-inf")

#Python numbers are infinte so they never overflows

print(math.pow(2,200))

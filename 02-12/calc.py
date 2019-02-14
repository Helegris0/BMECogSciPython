import sys
import math

n1 = int(input('First number: '))
n2 = int(input('Second number: '))

ari_mean = (n1 + n2) / 2
geo_mean = math.sqrt(n1 * n2)

print('Arithmetic mean: ' + str(ari_mean))
print('Geometric mean: ' + str(geo_mean))

def get_smaller(x, y):
  if (x < y):
    return x
  else:
    return y

print('Smaller number: ' + str(get_smaller(n1, n2)))

def get_greatest_common_divisor(x, y):
  smaller = get_smaller(x, y)

  for i in range(smaller, 0, -1):
    if (x % i == 0 and y % i == 0):
      return i

print('Greatest common divisor: ' + str(get_greatest_common_divisor(n1, n2)))


# Program to calculate gcd of 2 numbers


# Function to demonstrate basic Euclidean Algorithm

def gcd(a, b):
 if a == 0:
  return b

 return gcd(b % a, a)

# Function to demonstrate working of extended  Euclidean Algorithm

def gcdExtended(a, b):
 # Base Case
 if a == 0:
  return b, 0, 1

 gcd, x1, y1 = gcdExtended(b % a, a)

 # Update x and y using results of recursive call
 x = y1 - (b // a) * x1
 y = x1

 return gcd, x, y

if __name__ == '__main__':
 a = 10
 b = 15
 print("gcd(", a, ",", b, ") = ", gcd(a, b))

 a = 31
 b = 2
 print("gcd(", a, ",", b, ") = ", gcd(a, b))

 print("The extended Euclidean algorithm also finds integer coefficients x and y such that: ax + by = gcd(a, b) ")

 a, b = 95, 17
 g, x, y = gcdExtended(a, b)

 print(a, "(", x, ")", "+", b, "(", y, ") = ",  g)
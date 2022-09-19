# sqrt.py


# Input
n = float(input("Enter a nonnegative value: "))
while n < 0:
  n = float(input("I SAID NONNEGATIVE: "))
epsilon = float(input("Enter another nonnegative value: "))
while epsilon < 0:
  epsilon = float(input("I SAID NONNEGATIVE: "))

# Computation
lastGuess = n
x = n/2
while abs(lastGuess - x) > epsilon:
  lastGuess = x
  x = (x + n/x) / 2

# Output
print("By approximation, the square root of", n, "is", x)
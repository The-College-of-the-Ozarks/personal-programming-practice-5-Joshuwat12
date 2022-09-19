# even_sum.py


# Input
a = int(input("Enter an integer: "))
b = int(input("Enter another integer, ideally greater than the first one: "))

# Computation
total = 0
n = a + 1
while n < b:
  if n % 2 == 0:
    total += n
  n += 1

# Output
print("The sum of all even integers from", a, "to", b, "is", total)
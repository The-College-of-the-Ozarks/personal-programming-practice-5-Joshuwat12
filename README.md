# Programming 1: Personal Programming Practice 5

---

Write programs to tackle the following problems. Use the specified .py file (in **bold**) for each part (each file should be created automatically in your repository). You may discuss and collaborate with your peers, but you should submit your own code and fully understand all code you submit. If you work with others on one of the parts, cite your collaborators in a comment near the top of that file.

1. In **even_sum.py**, write a program which takes two integer inputs and outputs the sum of all the even integers strictly between them (that is, don't include either endpoint in your sum). Your output should clearly describe the number you computed.
2. In **sqrt.py**, you will write a program to approximate the square root of a positive number.

First, use a loop to ensure the user gives valid input number n.

Then the algorithm proceeds as follows:
1. Make an initial guess of n/2.
2. Given your current guess x, make a new guess (x + n/x)/2
3. Repeat step 2 until you are "close enough" to the correct value. You may use any of the following measures of "close enough." Option i. will be easiest to implement and will earn full points, bonus may be earned by implementing any of options ii - iv (arranged easiest to hardest). *Remember, the abs() function will be useful.*

    1. x**2 is within 0.1 of the actual value of n
    2. x**2 is within epsilon of the actual value of n, where epsilon is a nonnegative number input by the user
    3. x is within 0.001 of your previous guess
    4. x is within epsilon of your previous guess, where epsilon is a nonnegative number input by the user

Finally, output your approximation of sqrt(n).

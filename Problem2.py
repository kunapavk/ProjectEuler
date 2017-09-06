# Sum of even Fibonacci numbers below 4 million
sum_val = 0
term1, term2 = 0, 1
while (term1 < 4000000 and term2 < 4000000):
    term2, term1 = term2 + term1, term2
    if (term2 % 2 is 0):
        sum_val += term2
print(sum_val)

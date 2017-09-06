# Sum of multiples of 3 and 5
sum_val = 0
for i in range(1000):
    if (i % 3 is 0):
        sum_val += i
        continue
    elif (i % 5 is 0):
        sum_val += i
print(sum_val)  

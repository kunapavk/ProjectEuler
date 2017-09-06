# Largest prime factor of 600851475143
max_val = 0
def is_prime(val):
    for i in range(2,(val // 2) + 1):
        if (val % i == 0):
            return False
    return True
actual_val = 600851475143
for i in range(2, (actual_val // 2) + 1):
    if (is_prime(i)):
        if (actual_val % i == 0):
            max_val = i
            print(max_val)
print(max_val)

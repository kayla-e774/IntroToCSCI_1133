# Kayla Engelstad
# ID: 5245863
# Lab Section 22

def sequence(n):
    sum1 = 0
    if n == 1:
        return sum1 + 1
    else:
        sum1 = (1 / (n**3)) + sequence(n - 1)
        print(sum1)
    return sum1

n = int(input("Enter n value: "))
results = sequence(n)
print(results)

#loop summation practice code

total = 0

for n in range(0, 101): #last number gets cut
    total = total + n
    print("After adding",n,"the sum is",total)

print("The total sum is",total)
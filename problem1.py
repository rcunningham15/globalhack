sum = 0
for x in range(1,1000):
    if (int(x) % 3 == 0) or (int(x) % 5 == 0):
        sum = sum + x
print(sum)
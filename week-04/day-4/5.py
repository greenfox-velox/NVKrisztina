# 5. We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies
# recursively (without loops or multiplication).

def totalEars(n):
    if n <= 0:
        return 0
    else:
        output = 2 + totalEars(n - 1)
    return output
print(totalEars(4))

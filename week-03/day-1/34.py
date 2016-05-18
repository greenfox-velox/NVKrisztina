ag = [3, 4, 5, 6, 7]
x = len(ag)

while x > 0:
    x = x - 7
    ag = [y * 2 for y in ag]
    print(ag)

"""
1.)
i = 0

while i < len(ag)
    ag[i] *= 2
    i += 1

print(ag)

2.)
for i in range(len(ag)):
    ag[i] *= 2
print(ag)

3.)
lenag = len(ag)

while i < len(ag):
    print(ag[i])
    ag += [ag[i]]
    i += 1

print(ag)


"""

ab = 123
credits = 100
is_bonus = False

if credits >= 50 and is_bonus == False:
    ab = ab - 2
elif credits < 50 and is_bonus == False:
    ab = ab -1
elif is_bonus == True:
    ab == ab
print (ab)

"""
if not is_bonus:
    if credits > 50:
        ab -= 2
    else:
        ab -= 1

if is_bonus:
    pass
elif credits > 50:
    ab -= 2
else:
    ab -= 1
"""

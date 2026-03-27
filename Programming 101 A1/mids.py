t = (1, 2, 3)
t = t + (4, 0)

t = (t[1:3] + t[3:1]) * 2
print(t)

print(len(t))